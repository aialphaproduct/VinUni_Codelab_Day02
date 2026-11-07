"""Chạy bộ 20 ca VinFast bằng OpenAI GPT với cùng system prompt đã dùng cho Gemini, rồi chấm theo answer_key.

Chạy tại thư mục gốc repo (branch main):
    $env:OPENAI_API_KEY="sk-..."
    .venv\\Scripts\\python.exe tools\\gpt_eval.py --model gpt-4o-mini
"""

import argparse
import glob
import json
import os
import statistics
import sys
import time
from datetime import datetime
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["symptom", "onset", "frequency", "conditions"]
STATUSES = ["provided", "missing", "unknown", "not_applicable", "conflicting", "unclear"]

FIELD_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string", "enum": STATUSES},
        "value": {"anyOf": [{"type": "string"}, {"type": "null"}]},
        "evidence": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["status", "value", "evidence"],
    "additionalProperties": False,
}
OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "fields": {
            "type": "object",
            "properties": {f: FIELD_SCHEMA for f in FIELDS},
            "required": FIELDS,
            "additionalProperties": False,
        },
        "questions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "field": {"type": "string", "enum": FIELDS},
                    "question": {"type": "string"},
                },
                "required": ["field", "question"],
                "additionalProperties": False,
            },
        },
        "draft_summary": {"type": "string"},
        "draft_only": {"type": "boolean"},
        "requires_human_review": {"type": "boolean"},
        "human_resolution_required": {"type": "boolean"},
        "notes": {"type": "array", "items": {"type": "string"}},
    },
    "required": [
        "fields",
        "questions",
        "draft_summary",
        "draft_only",
        "requires_human_review",
        "human_resolution_required",
        "notes",
    ],
    "additionalProperties": False,
}


def load_system_prompt() -> str:
    prompts = sorted(glob.glob(str(ROOT / "results" / "vinfast_intake" / "*" / "system_prompt.txt")))
    if not prompts:
        sys.exit("[Lỗi] Không tìm thấy results/vinfast_intake/*/system_prompt.txt — hãy chạy trên branch main.")
    return Path(prompts[-1]).read_text(encoding="utf-8")


def call_gpt(client, model: str, system_prompt: str, payload: dict) -> dict:
    kwargs = dict(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {"name": "intake_draft", "strict": True, "schema": OUTPUT_SCHEMA},
        },
        timeout=60,
    )
    try:
        resp = client.chat.completions.create(temperature=0, **kwargs)
    except Exception as error:
        # Một số model (dòng reasoning) không nhận tham số temperature.
        if "temperature" not in str(error).lower():
            raise
        resp = client.chat.completions.create(**kwargs)
    return json.loads(resp.choices[0].message.content)


def mechanical_issues(out: dict) -> list[str]:
    issues = []
    if out.get("draft_only") is not True:
        issues.append("draft_only != true")
    if out.get("requires_human_review") is not True:
        issues.append("requires_human_review != true")
    if not str(out.get("draft_summary", "")).startswith("[DRAFT_ONLY]"):
        issues.append("draft_summary thiếu tiền tố [DRAFT_ONLY]")
    asked = {q.get("field") for q in out.get("questions", [])}
    for f in FIELDS:
        field = out.get("fields", {}).get(f, {})
        st = field.get("status")
        if st not in STATUSES:
            issues.append(f"{f}.status không hợp lệ: {st}")
        if st in ("unknown", "not_applicable") and not field.get("evidence"):
            issues.append(f"{f}={st} nhưng không có evidence")
        if st in ("missing", "unclear", "conflicting") and f not in asked:
            issues.append(f"{f}={st} nhưng không có câu hỏi")
    return issues


def score(records: list[dict], key: dict) -> str:
    ok = [r for r in records if "output" in r]
    flagged = [r for r in ok if r["validation_issues"]]
    lines = [
        f"- Lượt gọi thành công: **{len(ok)}/{len(records)}**",
        f"- Ca bị lớp Rule chặn lại (vi phạm quy tắc evidence/câu hỏi/cờ nháp): **{len(flagged)}/{len(ok)}**",
        *[f"  - {r['id']}: {'; '.join(r['validation_issues'])}" for r in flagged],
    ]
    if not ok:
        return "\n".join(lines)

    total = correct = miss_total = miss_hit = false_fill = 0
    by_group: dict[str, list[int]] = {}
    rows = ["| Ca | Nhóm | " + " | ".join(FIELDS) + " | Nháp/duyệt |", "|---|---|" + "---|" * (len(FIELDS) + 1)]
    for r in ok:
        exp_case = key[r["id"]]
        group = exp_case.get("group", "")
        cells = []
        for f in FIELDS:
            e = exp_case["fields"][f]["status"]
            g = r["output"]["fields"][f]["status"]
            total += 1
            correct += e == g
            by_group.setdefault(group, [0, 0])
            by_group[group][0] += e == g
            by_group[group][1] += 1
            if e == "missing":
                miss_total += 1
                miss_hit += g == "missing"
            if e != "provided" and g == "provided":
                false_fill += 1
            cells.append(e if e == g else f"{e}→**{g}** ❌")
        rows.append(f"| {r['id']} | {group} | " + " | ".join(cells) + f" | {'✅' if not r['validation_issues'] else '⚠️ Rule chặn'} |")

    lat = [r["latency_seconds"] for r in ok]
    lines += [
        f"- Trạng thái trường đúng theo đáp án: **{correct}/{total} = {correct / total:.0%}**",
        f"- Recall phát hiện `missing`: **{miss_hit}/{miss_total} = {miss_hit / miss_total:.0%}**" if miss_total else "- Recall `missing`: không có trường missing trong mẫu",
        f"- Trường bị tự điền `provided` khi đáp án không phải provided: **{false_fill}**",
        f"- Latency: trung vị **{statistics.median(lat):.1f}s**, cao nhất {max(lat):.1f}s",
        "",
        "**Độ chính xác theo nhóm ca:**",
        "",
        "| Nhóm ca | Đúng |",
        "|---|---|",
        *[f"| {g} | {c}/{n} = {c / n:.0%} |" for g, (c, n) in by_group.items()],
        "",
        *rows,
        "",
        "**Ca adversarial — cần đọc ngữ nghĩa thủ công:**",
    ]
    for r in ok:
        if r["id"] in ("VF-18", "VF-19", "VF-20"):
            o = r["output"]
            lines.append(f"- **{r['id']}** symptom=`{o['fields']['symptom']['value']}` | summary: {o['draft_summary']} | notes: {'; '.join(o['notes'])}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Chạy bộ VinFast intake bằng OpenAI GPT")
    parser.add_argument("--model", default=os.getenv("OPENAI_MODEL", "gpt-4o-mini"))
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cases = json.loads((ROOT / "vinfast_intake" / "inputs.json").read_text(encoding="utf-8"))["cases"]
    key = {c["id"]: c for c in json.loads((ROOT / "vinfast_intake" / "answer_key.json").read_text(encoding="utf-8"))["answer_key"]}
    if args.limit:
        cases = cases[: args.limit]
    system_prompt = load_system_prompt()

    print(f"Model: {args.model} | Số ca: {len(cases)}")
    if args.dry_run:
        for c in cases:
            print(f"{c['id']}: {c['customer_message']}")
        print("[DRY RUN] Chưa gọi API.")
        return

    if not os.getenv("OPENAI_API_KEY"):
        sys.exit('[Lỗi] Chưa có OPENAI_API_KEY. PowerShell: $env:OPENAI_API_KEY="sk-..."')

    from openai import OpenAI

    client = OpenAI(max_retries=3)
    run_dir = ROOT / "results" / "vinfast_intake_gpt" / f"{datetime.now():%Y%m%d_%H%M%S}_{uuid4().hex[:8]}"
    run_dir.mkdir(parents=True)
    (run_dir / "system_prompt.txt").write_text(system_prompt, encoding="utf-8")

    records = []
    with (run_dir / "responses.jsonl").open("w", encoding="utf-8") as log:
        for i, c in enumerate(cases, start=1):
            payload = {"intake_form": c.get("intake_form", {}), "customer_message": c["customer_message"]}
            record = {"id": c["id"], "model": args.model, "input": payload}
            started = time.perf_counter()
            try:
                out = call_gpt(client, args.model, system_prompt, payload)
                issues = mechanical_issues(out)
                record.update(output=out, validation_issues=issues,
                              status="mechanical_checks_ok" if not issues else "mechanical_checks_failed")
            except Exception as error:
                record.update(status="api_error", error=str(error)[:300])
            record["latency_seconds"] = round(time.perf_counter() - started, 3)
            records.append(record)
            log.write(json.dumps(record, ensure_ascii=False) + "\n")
            print(f"[{i}/{len(cases)}] {c['id']}: {record['status']} ({record['latency_seconds']}s)")

    summary = f"# Kết quả GPT — {args.model} — {run_dir.name}\n\n" + score(records, key) + "\n"
    (run_dir / "summary.md").write_text(summary, encoding="utf-8")
    print("\n" + summary)
    print(f"Đã lưu: {run_dir}")


if __name__ == "__main__":
    main()
