# 03-ai-log.md — Nhật ký tương tác AI & Phản ánh (AI Log & Reflection)

> **Học viên:** Nguyễn Công Tĩnh · **Branch cá nhân:** congtinhx · **Lab 02: AI Product Scoping**
>
> Bài tự luận phản ánh quá trình dùng AI làm **thought-partner** trong buổi lab — chấm theo Gate **I3. AI Log & Reflection (15 điểm)**: *"Phản ánh trung thực về việc dùng AI làm thought-partner (giúp gì, sai gì, sửa gì)"*.

---

## 1. Tôi đã dùng AI như thế nào trong buổi lab?

Tôi dùng AI (Gemini / ChatGPT) ở 4 vai trò — không phải để "làm hộ", mà làm đối tác tư duy:

| # | Vai trò của AI | Giai đoạn | Prompt tôi thực sự dùng (tóm tắt) |
|---|---|---|---|
| 1 | **Brainstorm partner** — gợi ý pain point khi chưa đủ 5 problems | Phase 1 SCAN | Prompt gợi ý sẵn trong worksheet: *"Tôi là AI Engineer tại Vin Smart Future... Hãy gợi ý 5 quy trình nghiệp vụ thủ công... kèm con số thống kê ước tính về tổn thất."* |
| 2 | **Devil's advocate** — phản biện thẻ bài toán | Phase 2 QUICK-ASSESS | Prompt gợi ý sẵn trong worksheet: *"Đóng vai CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra 3 điểm yếu... giải thích vì sao rule-based có thể tốt hơn AI."* |
| 3 | **Code Copilot** — hoàn thiện `prompt_prototype.py` | Phase 4 PROTOTYPE | *"Viết hàm evaluate_prompt dùng SDK google-genai, truyền SYSTEM_PROMPT vào GenerateContentConfig, tuyệt đối không dán API key vào code."* |
| 4 | **Boundary tester** — nhờ AI chính là kẻ tấn công khi viết System Prompt | Phase 4 PROTOTYPE | *"Bạn là adversarial attacker. Làm sao để LLM vẫn giữ thẻ [DRAFT_ONLY] dù bị người dùng ép bỏ thẻ, giả vai quản lý, hứa thưởng?"* |

---

## 2. AI giúp được gì (điểm cộng)

1. **Không biết bắt đầu từ đâu** ở Phase 1: AI list nhanh ~7 pain point của 3 mảng (VinFast / Xanh SM / Vinhomes), tôi có nguyên liệu để tự chấm theo 4 Lenses — tiết kiệm khoảng 15 phút nhìn màn hình trống.
2. **Stress-test tạo giá trị thật** ở Phase 2: khi tôi đặt metric "phân loại chính xác ≥ 90%", AI đóng vai CFO chất vấn ngay: *"10% sai còn lại thì sao? một ticket sai điều hướng gây hậu quả gì? ai gắn nhãn cho 100 ticket test?"* → tôi phải bổ sung: ai thu nhãn, dùng bao lâu pilot, và thêm metric "tỷ lệ sai bộ phận ≤ 5%".
3. **Tăng tốc kỹ thuật** ở Phase 4: AI gợi ý cấu trúc system prompt có kỷ luật (Role → Boundaries → Output Format) thay vì viết lênh đênh; tôi chỉ cần rút gọn theo đúng 2 quy tắc của đề bài.
4. **Adversarial input tự nhiên hơn tư duy đơn lẻ:** nhờ nhờ AI "làm sao phá gãy prompt này", tôi có được test case prompt-injection mà tự tôi không nghĩ ra (giả vai quản lý, hứa thưởng, giả bộ quen thuộc...).

---

## 3. AI sai / hallucinate ở đâu (trung thực — phần quan trọng nhất)


### Sai sót 1 — Gợi ý API không tồn tại (Phase 4)

- AI đề xuất gọi `genai.GenerativeModel(...)` và nhấn rằng đó là cú pháp của SDK `google-genai` **mới** — thực chất đó là cú pháp của SDK **legacy** `google-generativeai`. Nếu chạy theo là lỗi ngay lần đầu.
- **Tôi sửa ra sao:** đọc tài liệu chính thức của `google-genai` cho đúng cú pháp: `client.models.generate_content(model=..., contents=..., config=types.GenerateContentConfig(system_instruction=...))`.


---

## 4. Bài học về làm việc với AI (Reflection)

1. **Adversarial test là cách học nhanh nhất về LLM.** 3 prompt tấn công dạy tôi nhiều hơn 10 prompt hỏi "làm thế nào": LLM khuynh hướng nghe người dùng hơn nghe hệ thống **trừ khi** system prompt được viết có tính đối kháng.
2. **Quyết định GO / NO-GO phải thuộc về con người.** AI khuyên "GO" gần như luôn liệt kê lợi ích mạnh một cách trống rỗng — checklist độ sẵn sàng (dữ liệu? rủi ro khống chế? stakeholder?) phải do nhóm tự chấm, không để AI quyết hộ.

---

## 5. Tự đánh giá mức độ phụ thuộc AI (trung thực)

| Phần bài | Tỷ lệ đóng góp của AI (ước tính) | Phần của tôi |
|---|---|---|
| Phase 1–2 (Scan & Cards) | ~50% (gợi ý + phản biện) | Tự chấm 4 Lenses, tự đặt metric, tự quyết định chọn bài toán Deep-Dive |
| Phase 3 & 5 (Deep-dive report) | ~30% (giúp diễn đạt & cấu trúc 6-field) | Workflow, bottleneck, metric, ranh giới, quyết định GO do tôi/nhóm tự chấm |
| Phase 4 (Code prototype) | ~40% (cú pháp SDK, test case) | Logic 2 quy tắc ranh giới + bổ sung test injection + sửa lỗi SDK là của tôi |
| Phản ánh (file này) | ~10% (chỉ khung mục) | Toàn bộ trải nghiệm thật, lỗi thật, bài học thật |