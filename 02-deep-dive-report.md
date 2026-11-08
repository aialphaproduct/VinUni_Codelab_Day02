# VinFast Service Intake Co-pilot — "Hỏi đúng ngay từ lần đầu"

**Tên nhóm:** Simple-Tech
**Thành viên nhóm:**
| # | Họ và tên | Email |
|---|-----------|-------|
| 1 | Lưu Thanh Mỹ (Trưởng nhóm) | data97688@gmail.com |
| 2 | Lưu Văn Việt Đức | luuvanvietduc@gmail.com |
| 3 | Nguyễn Công Tĩnh | tinh22102004@gmail.com |
| 4 | Vũ Trí Dũng | dungvutri25@gmail.com |
| 5 | Phạm Quang Trường | truongpham090325@gmail.com |
| 6 | Khổng Tiến Dương | khongtienduongcv@gmail.com |

**Người thực hiện nội dung gốc:** Lưu Văn Việt Đức · **Biên tập và bổ sung đo lường:** cả nhóm
**Ngày cập nhật:** 08/11/2026
**Phạm vi đóng góp:** Báo cáo tổng hợp đại diện cho **nhóm Simple-Tech** trên `main`. Bài toán: Card #1 trong [01-problem-scan.md](01-problem-scan.md). Bản gốc của Đức, bộ dữ liệu và log nằm ở [`phu-luc-vinfast/`](phu-luc-vinfast/02-deep-dive-report.md).

---

## Mở đầu — một câu "Điều hòa xe tôi không mát"

> *Tình huống minh họa, dựng từ ca VF-01 trong bộ thử của nhóm.*

Một khách hàng đặt lịch sửa chữa trên ứng dụng VinFast và gõ vào ô mô tả: **"Điều hòa xe tôi không mát, nhờ kiểm tra giúp."**

Câu này đủ để đặt lịch, nhưng chưa đủ để kỹ thuật viên bắt đầu đúng hướng. Không mát **từ khi nào**? **Lúc nào cũng vậy** hay chỉ thỉnh thoảng? **Trong điều kiện nào** — đỗ ngoài nắng, chạy đường dài, hay ngay khi vừa khởi động? Cố vấn dịch vụ có hai lựa chọn, và cả hai đều tốn kém:

- **Hỏi lại khách** → thêm một vòng nhắn tin, khách phải chờ, phiếu tiếp nhận chậm hoàn thiện.
- **Không hỏi** → kỹ thuật viên kiểm tra theo phỏng đoán, dễ phải hẹn khách quay lại lần hai.

Ngành dịch vụ ô tô đo chuyện này bằng một chỉ số quen thuộc: **tỉ lệ sửa đúng ngay lần đầu (first-time-fix)**. Thông tin tiếp nhận càng đầy đủ, chỉ số này càng cao.

**Câu hỏi của nhóm:** AI có thể giúp cố vấn **hỏi đúng câu cần hỏi ngay từ lần đầu** — mà không đoán thay khách, và không chẩn đoán thay kỹ thuật viên — hay không?

> ### ⏱ Tóm tắt 30 giây
> - **Bài toán:** khách mô tả hiện tượng của xe bằng ngôn ngữ đời thường, thường thiếu thời điểm, tần suất, điều kiện xuất hiện; cố vấn phải tự phát hiện chỗ thiếu và hỏi lại.
> - **Giải pháp:** trợ lý đọc mô tả, đánh dấu từng mục `có / thiếu / khách không biết / mâu thuẫn`, kèm trích dẫn nguyên văn làm căn cứ, rồi soạn sẵn câu hỏi làm rõ — **cố vấn duyệt trước khi gửi**.
> - **Đã đo trên 20 ca giả lập:** GPT-4o-mini đúng **74%** trạng thái các mục, phát hiện **65%** mục thiếu; chặn được **3/3** kiểu tấn công; một lớp kiểm tra bằng code bắt thêm **15/21** lỗi của model.
> - **Quyết định:** **NOT YET** — mục tiêu là 90%, và nhóm chỉ ra được chính xác 3 việc cần làm để đạt (mục 5.2).

---

### Vì sao nhóm chọn đề tài này

Sáu thành viên tự scoping sáu đề tài trên branch riêng (xem [01-problem-scan.md](01-problem-scan.md)). Đề tài VinFast của Đức được chọn vì hội đủ bốn điều kiện mà các đề tài khác chỉ có một phần:

| Tiêu chí | Đề tài VinFast |
|---|---|
| **Nỗi đau có thật, chưa được giải quyết** | Biểu mẫu đặt lịch của VinFast có ô mô tả tự do [S1–S3], nhưng không kiểm tra được nội dung đó đã đủ để chẩn đoán chưa |
| **Thật sự cần LLM** | Mô tả là tiếng Việt đời thường ("kêu cụp cụp", "máy lạnh yếu", "xe bị ì") — Rule không đọc hiểu được |
| **Đo được** | Có bộ 20 ca giả lập kèm đáp án, đã chạy trên 2 model |
| **Ranh giới an toàn rõ** | AI tuyệt đối không chẩn đoán, không báo giá, không tự điền điều khách chưa nói |

Nhóm cũng đã thử nâng cấp đề tài Xanh SM (xử lý sự cố pin) bằng bộ 24 ca và 4 lượt đo. Khi đối chiếu thực tế, tài xế đã **tự tra trạm sạc trên app**, nên phạm vi bài toán còn rất hẹp. Thử nghiệm đó được giữ ở [`phu-luc-xanhsm/`](phu-luc-xanhsm/02-deep-dive-report.md) vì đem lại một bài học kiến trúc dùng thẳng cho bài này (mục 3.1).

### Đóng góp của từng thành viên

| Thành viên | Đề tài cá nhân (branch) | Đóng góp vào bài nhóm |
|---|---|---|
| **Lưu Văn Việt Đức** | **VinFast — tiếp nhận dịch vụ** (`vietduc`) | **Tác giả đề tài chính:** scan, Quick Cards, deep-dive, bộ dữ liệu 20 ca + đáp án, prototype và log Gemini |
| Lưu Thanh Mỹ (Trưởng nhóm) | Xanh SM — sự cố pin (`luuthanhmy`) | Tạo repo, rà soát 6 branch, tổng hợp `main`; thử nghiệm Xanh SM (phụ lục) cho bài học Rule + LLM |
| Nguyễn Công Tĩnh | Vinhomes – Vinpearl — một đầu mối hỗ trợ (`nguyencongtinh`) | Quick Card #3; góc nhìn trải nghiệm khách hàng "một cửa" |
| Vũ Trí Dũng | Vinmec — hồ sơ bảo hiểm, đối soát viện phí (`VuTriDung`) | Góp mảng y tế vào bảng Scan chung |
| Phạm Quang Trường | Xanh SM — lý do hủy chuyến (`PhamQuangTruong`) | Góp bài toán phân tích offline vào bảng Scan chung |
| Khổng Tiến Dương | Vinhomes — phân loại khiếu nại (`khongtienduong`) | Góp ví dụ bài toán Rule-based router có thể đủ tốt |

**Phần cả nhóm cùng làm khi tổng hợp:** chấm điểm log Gemini, chạy đủ 20 ca trên GPT-4o-mini, xây lớp kiểm tra bằng code, phân tích lỗi và biên tập báo cáo.

---

## 1. Phase 3.1 — Current-State Workflow

> Quy trình dưới đây là **mô hình giả định** dựa trên các bước công khai của ứng dụng và biểu mẫu đặt lịch VinFast [S1–S3]; chưa được VinFast xác nhận.

```text
┌───────────────┐        ┌────────────────────┐        ┌─────────────────────┐
│ Khách gửi biểu│ 🔄     │ Cố vấn đọc mô tả,  │        │ Cần làm rõ?         │
│ mẫu + mô tả   │ ─────→ │ đối chiếu checklist│ ─────→ │                     │
│ tự do         │        │ 🔴 bottleneck      │        └──────┬──────────┬───┘
└───────────────┘        └────────────────────┘          Có   │          │ Không
                                   ▲                          ▼          ▼
                                   │ 🔄             ┌──────────────┐  ┌──────────────┐
                         ┌─────────┴─────────┐      │ Cố vấn soạn  │  │ Hoàn thiện,  │
                         │ Khách phản hồi    │ ←─── │ câu hỏi      │  │ bàn giao     │ 🔄
                         │ (chờ: phút → giờ) │  🔄  │ 🔴 bottleneck│  │ cho kỹ thuật │
                         └───────────────────┘      └──────────────┘  └──────────────┘
```

| Công đoạn | Ai làm | Ước lượng / lượt *(giả định)* |
|---|---|---|
| Đọc mô tả, đối chiếu checklist 4 mục 🔴 | Cố vấn | 2–3 phút |
| Soạn câu hỏi làm rõ 🔴 | Cố vấn | 2–4 phút |
| Chờ khách phản hồi | Khách | vài phút đến vài giờ *(không tính vào thao tác)* |
| Đọc phản hồi, cập nhật | Cố vấn | 1–2 phút |
| Hoàn thiện, bàn giao phiếu | Cố vấn → kỹ thuật viên 🔄 | 2–3 phút |
| **Tổng thao tác chủ động (1 vòng hỏi)** | | **≈ 7–12 phút** — mỗi vòng hỏi thêm cộng ≈ 3–6 phút |

- 🔴 **Bottleneck:** đọc hiểu mô tả tự do và đặt đúng câu hỏi. Hỏi thiếu thì phiếu bàn giao thiếu; hỏi thừa thì khách khó chịu.
- 🔄 **Handoff:** khách ↔ cố vấn (mỗi vòng hỏi đáp), cố vấn → kỹ thuật viên (bàn giao phiếu).
- ⏱ Số phút là **ước lượng của nhóm, chưa bấm giờ thực tế**. Sơ đồ trực quan: [04-workflow-diagram.png](04-workflow-diagram.png).

## 2. Phase 3.2 — Problem Statement (6 trường)

| Trường | Nội dung |
|---|---|
| **1. Actor / Operator** | **Cố vấn dịch vụ** tại xưởng VinFast — người tiếp nhận yêu cầu sửa chữa. Khách hàng là người cung cấp và xác nhận thông tin. |
| **2. Current Workflow** | Khách đặt lịch trên app, gõ mô tả tự do → cố vấn đọc và đối chiếu checklist → xác định chỗ cần làm rõ → hỏi khách (có thể nhiều vòng) → hoàn thiện phiếu và bàn giao cho kỹ thuật viên. |
| **3. Bottleneck** | Đọc hiểu mô tả đời thường và đặt **đúng** câu hỏi: không bỏ sót mục quan trọng, không hỏi lại điều khách đã nói, không vô tình gợi ý chẩn đoán. |
| **4. Business Impact** | *Giả thuyết cần kiểm chứng:* mỗi vòng hỏi lại thêm ≈ 3–6 phút thao tác và kéo dài thời gian khách chờ; phiếu thiếu thông tin làm giảm tỉ lệ sửa đúng ngay lần đầu. Chưa có số liệu VinFast để lượng hóa chi phí. |
| **5. Success Metric** | Trên ≥ 20 ca có đáp án: **(a)** phát hiện đúng **≥ 90%** mục thiếu; **(b)** **0** dữ kiện tự điền không có căn cứ; **(c)** **0** hành động vượt quyền; **(d)** giảm **≥ 30%** thời gian thao tác chủ động so với checklist thủ công (cần đo). |
| **6. Operational Boundary** | **Được phép:** trích xuất dữ kiện **kèm trích dẫn nguyên văn**, đánh dấu mục thiếu/mâu thuẫn, soạn câu hỏi nháp. **Không được phép:** chẩn đoán nguyên nhân, chỉ định thay phụ tùng, báo giá, cam kết bảo hành, tự gửi câu hỏi, tuyên bố phiếu đã duyệt, xác nhận lịch hẹn. **Cố vấn duyệt mọi bản nháp; kỹ thuật viên chịu trách nhiệm chẩn đoán.** |

### 2.1. Biểu mẫu đã có, vì sao vẫn cần trợ lý?

| | Biểu mẫu đặt lịch hiện có [S3] | Intake Co-pilot của nhóm |
|---|---|---|
| Kiểm tra được | Trường có cấu trúc: mẫu xe, số km, biển số | **Nội dung** của ô mô tả tự do |
| Biết mô tả đã đủ chưa? | Không | Có — theo 4 mục: hiện tượng, thời điểm, tần suất, điều kiện |
| Phát hiện mâu thuẫn giữa biểu mẫu và lời khách? | Không | Có (cần thêm luật code — mục 5.2) |
| Gợi ý câu hỏi tiếp theo | Không | Có, cố vấn duyệt trước khi gửi |

Trợ lý **không thay biểu mẫu**: phần có cấu trúc vẫn do biểu mẫu và Rule kiểm tra; LLM chỉ đảm nhận phần mà biểu mẫu không làm được — **đọc hiểu lời khách**.

## 3. Phase 3.3 — AI Fit & Future-State Flow

### 3.1. Rule, LLM, Hybrid hay Agent?

| Phương án | Làm tốt | Không làm được | Bằng chứng | Vai trò |
|---|---|---|---|---|
| **Biểu mẫu / checklist thủ công** | Rẻ, ổn định | Không đọc được mô tả tự do | — | Phương án đối chứng |
| **Rule** | Kiểm tra trường trống, định dạng, so khớp giá trị | Không hiểu "kêu cụp cụp" là hiện tượng gì | — | Lớp kiểm tra đầu vào và đầu ra |
| **LLM** | Đọc hiểu, trích dẫn, soạn câu hỏi tự nhiên | Có thể gán nhãn sai, tự chọn giá trị khi mâu thuẫn | GPT-4o-mini: 74% trạng thái đúng | Lõi đọc hiểu |
| **Hybrid: Rule + LLM + HITL** ✅ | Kết hợp cả hai | Phụ thuộc chất lượng luật | Lớp Rule bắt **15/21** lỗi của LLM | **Lựa chọn của nhóm** |
| **Agentic Loop** | Tự gọi nhiều công cụ | Không cần tự lập kế hoạch; tăng quyền truy cập và rủi ro | — | Không chọn |

**Bài học mang sang từ thử nghiệm Xanh SM:** khi để LLM tự quyết ngưỡng pin "< 5%", model sai ở mức 6% và 8% dù prompt đã ghi rõ; chuyển quyết định đó sang code thì đạt 24/24 ca ([phụ lục](phu-luc-xanhsm/02-deep-dive-report.md)). Nguyên tắc rút ra áp dụng thẳng cho VinFast: **việc gì có đáp án tất định (so khớp giá trị, kiểm tra trường) thì giao cho code; LLM chỉ làm phần cần đọc hiểu ngôn ngữ.**

### 3.2. Future-State Flow

```text
Khách gửi biểu mẫu + mô tả
        │
        ▼
🟩 RULE: kiểm tra trường bắt buộc, định dạng
        │
        ▼
🟦 LLM: đánh dấu 4 mục (có / thiếu / không biết / không áp dụng / mâu thuẫn),
        mỗi nhận định kèm trích dẫn nguyên văn; soạn câu hỏi nháp
        │
        ▼
🟩 RULE kiểm tra đầu ra:
   • "không biết / không áp dụng" phải có trích dẫn
   • mục "thiếu / mâu thuẫn" phải có câu hỏi đi kèm
   • giá trị trên biểu mẫu khác lời khách → buộc gắn "mâu thuẫn"   (cần bổ sung)
   • JSON sai, thiếu cờ nháp → chặn ──────────────┐
        │                                         ▼
        ▼                                  ↩️ FALLBACK: cố vấn dùng checklist thủ công
🟨 HITL: cố vấn đối chiếu trích dẫn, sửa,      (cả khi API lỗi hoặc chậm > 15 s)
         duyệt câu hỏi rồi mới gửi khách
        │
        ▼
Khách bổ sung → cố vấn xác nhận phiếu → bàn giao kỹ thuật viên
```

## 4. Phase 4 — Prompt Prototype & kết quả đo

### 4.1. Bộ thử

**20 ca giả lập** do Đức xây dựng, kèm đáp án tham chiếu cho từng mục ([`vinfast_intake/`](phu-luc-vinfast/vinfast_intake/README.md)):

| Nhóm ca | Ca | Kiểm tra |
|---|---|---|
| Mô tả ngắn, thiếu thông tin | VF-01–04 | Phát hiện đủ các mục thiếu |
| Đã có một phần | VF-05–08 | Không hỏi lại điều khách đã nói |
| Thông tin đầy đủ | VF-09–11 | Không hỏi thừa |
| Không biết / không áp dụng | VF-12–14 | Tôn trọng câu "tôi không nhớ", không ép khách trả lời |
| **Mâu thuẫn** biểu mẫu ↔ tin nhắn | VF-15–17 | Gắn "mâu thuẫn", **không tự chọn giá trị** |
| **Tấn công** | VF-18–20 | Không tự thêm triệu chứng, không chẩn đoán, không bỏ cờ nháp |

Đầu ra là JSON có cấu trúc: mỗi mục gồm `status`, `value`, `evidence` (trích dẫn nguyên văn); cùng `questions`, `draft_summary` bắt đầu bằng `[DRAFT_ONLY]`, cờ `draft_only` và `requires_human_review` luôn `true`.

### 4.2. Kết quả trên hai model

| Chỉ số | Gemini (`gemini-3.8-flash`) | GPT-4o-mini |
|---|---|---|
| Lượt gọi API thành công | 4/15 (27%) — lỗi 404/503/504 | **20/20** |
| Số ca đánh giá được | 4 ca dễ | **Đủ 20 ca** |
| Trạng thái mục đúng theo đáp án | 16/16 | **59/80 = 74%** |
| Phát hiện mục thiếu (recall) | 9/9 | **11/17 = 65%** ❌ (mục tiêu 90%) |
| Tự điền dữ kiện không có căn cứ | 0 | **3** — đều ở nhóm mâu thuẫn |
| Giữ cờ nháp + `[DRAFT_ONLY]` | 4/4 | **20/20** |
| Ca tấn công đạt (đọc ngữ nghĩa) | 1/1 | **3/3** |
| Thời gian phản hồi (trung vị) | 9,7 s | 3,4 s |

Trên 4 ca chung, Gemini đúng 16/16 còn GPT đúng 13/16 — Gemini chính xác hơn nhưng không ổn định; GPT ổn định nhưng chưa đạt ngưỡng. **Không model nào đủ điều kiện dùng một mình.**

Độ chính xác của GPT-4o-mini theo nhóm ca: mô tả ngắn 81% · một phần 75% · đầy đủ 83% · không biết/không áp dụng 75% · **mâu thuẫn 58%** · tấn công 67% (sai ở trạng thái mục, không phải ở ranh giới).

Log: [Gemini](phu-luc-vinfast/results/vinfast_intake/) · [GPT-4o-mini 20 ca](phu-luc-vinfast/results/vinfast_intake_gpt/20261107_233952_5d7843c5/summary.md).

### 4.3. 21 mục sai nói lên điều gì

| Kiểu lỗi | Số mục | Hậu quả | Lớp Rule bắt được? |
|---|---|---|---|
| Gắn "không áp dụng" **không kèm trích dẫn** (đáng lẽ là "thiếu") → bỏ luôn câu hỏi | 15 | Cố vấn quên hỏi khách | ✅ **15/15** |
| **Tự chọn một giá trị khi biểu mẫu và tin nhắn mâu thuẫn** | 3 | Phiếu bàn giao sai thông tin | ❌ chưa bắt được |
| Hỏi thừa | 3 | Thêm một câu hỏi | Không cần chặn |

**Ca đáng chú ý nhất — VF-17.** Biểu mẫu ghi *"chỉ khi xe đỗ ở chỗ bằng phẳng"*; khách lại nhắn cửa khó đóng *"mỗi lần xe đỗ trên dốc; khi xe đỗ ở chỗ bằng phẳng thì không bị"*. GPT ghi điều kiện theo biểu mẫu — **ngược hẳn lời khách** — và không bật cờ nào để cố vấn kiểm tra lại. Đây chính là loại lỗi mà một luật so khớp bằng code xử lý dễ dàng, đúng như bài học từ Xanh SM.

**Ranh giới an toàn giữ vững:** cả 3 ca tấn công (ép thêm triệu chứng "mùi khét", ép kết luận "mô tơ hỏng", ép bỏ nhãn nháp và xác nhận lịch) đều chỉ được ghi nhận trong `notes` như **yêu cầu bị từ chối**, không đi vào phiếu.

## 5. Phase 5 — Evaluate

### 5.1. AI Readiness Checklist

| Câu hỏi | Trạng thái | Căn cứ |
|---|---|---|
| Có dữ liệu mẫu và log để kiểm thử? | **Có một phần** | 20 ca giả lập có đáp án, log 2 model; chưa có hồ sơ tiếp nhận thật |
| Rủi ro khi AI sai có trong tầm kiểm soát? | **Có, đã đo một phần** | Cố vấn duyệt mọi bản nháp; lớp Rule bắt 15/21 lỗi; fallback checklist |
| Stakeholder sẵn sàng thay đổi quy trình? | **Chưa xác nhận** | Chưa phỏng vấn cố vấn dịch vụ VinFast |

### 5.2. Quyết định: NOT YET — kèm lộ trình 3 bước tới GO

- [ ] GO
- [x] **NOT YET**
- [ ] NO-GO

Nhóm chọn **chưa triển khai**, vì lý do đo được chứ không phải cảm tính: recall phát hiện mục thiếu mới đạt **65%**, thấp hơn mục tiêu **90%**, và còn **3 lỗi mâu thuẫn** lọt qua mọi lớp kiểm tra. Nhưng NOT YET ở đây không phải "dừng lại" — các lỗi đã được phân loại đủ rõ để biết chính xác cần làm gì:

| Bước | Việc cần làm | Nhắm vào lỗi nào | Điều kiện đạt |
|---|---|---|---|
| **1** | Luật code: giá trị trên biểu mẫu khác trích dẫn trong tin nhắn → buộc gắn "mâu thuẫn" và hiển thị cạnh nhau cho cố vấn | 3 lỗi tự chọn giá trị (VF-15–17) | 0 lỗi mâu thuẫn lọt qua |
| **2** | Chuyển luật "không áp dụng phải có trích dẫn" từ *chặn* sang *tự sửa về thiếu + thêm câu hỏi* | 15 lỗi bỏ sót câu hỏi | Recall ≥ 90% trên 20 ca cũ |
| **3** | Thêm ≥ 10 ca mới chưa từng dùng để tinh chỉnh; bấm giờ cố vấn làm thủ công và có trợ lý | Kiểm chứng không "học thuộc đề" | Recall ≥ 90% trên ca mới; giảm ≥ 30% thời gian |

Khi đạt cả ba bước, nhóm đề xuất **GO ở chế độ chạy song song (shadow mode)** tại một xưởng: trợ lý soạn song song, cố vấn vẫn làm như cũ, so sánh trên dữ liệu thật trước khi dùng chính thức.

## 6. Q&A dự kiến

| Câu hỏi | Trả lời |
|---|---|
| "Kết quả chỉ 65%, sao vẫn chọn đề tài này?" | Vì 65% là **số đo thật**, và nhóm biết chính xác phần còn thiếu nằm ở đâu: 15/21 lỗi đã có luật bắt được, 3 lỗi còn lại có cách xử lý tất định (mục 5.2). Một đề tài "đạt 100%" trên giấy nhưng không đo thì không nói lên được điều này. |
| "Dữ liệu giả lập có đáng tin?" | Đủ để kiểm tra hành vi và ranh giới, chưa đủ để kết luận hiệu quả vận hành — vì vậy quyết định là NOT YET. |
| "Sao dùng GPT khi đề yêu cầu Gemini?" | Code nộp bài vẫn dùng Gemini SDK. Gemini chỉ trả kết quả 4/15 lượt gọi, nên nhóm chạy đủ 20 ca trên GPT với **cùng system prompt và đáp án** để có số liệu so sánh. |
| "AI có chẩn đoán thay kỹ thuật viên không?" | Không. Ranh giới này giữ được ở cả 3 ca cố ý ép chẩn đoán. |
| "Biểu mẫu đã có ô mô tả rồi?" | Biểu mẫu nhận mô tả nhưng không biết mô tả đã đủ chưa. Trợ lý chỉ làm đúng phần đó (mục 2.1). |

## 7. Tài liệu và bằng chứng

- **[S1]** VinFast — Câu hỏi thường gặp về ứng dụng VinFast dành cho ô tô điện: https://vinfastauto.com/vn_vi/cau-hoi-thuong-gap/cau-hoi-xe-o-to/san-pham/ung-dung-vinfast
- **[S2]** VinFast — Hướng dẫn sử dụng tiện ích dịch vụ trên ứng dụng VinFast: https://vinfastauto.com/vn_vi/huong-dan-su-dung-tien-ich-dich-vu-tren-ung-dung-vinfast
- **[S3]** VinFast — Biểu mẫu đặt lịch dịch vụ bảo dưỡng: https://shop.vinfastauto.com/vn_vi/dat-lich-dich-vu-bao-duong.html
- Bộ dữ liệu 20 ca và đáp án: [`phu-luc-vinfast/vinfast_intake/`](phu-luc-vinfast/vinfast_intake/README.md)
- Log Gemini: [`phu-luc-vinfast/results/vinfast_intake/`](phu-luc-vinfast/results/vinfast_intake/) · Log GPT-4o-mini: [`phu-luc-vinfast/results/vinfast_intake_gpt/`](phu-luc-vinfast/results/vinfast_intake_gpt/20261107_233952_5d7843c5/summary.md)
- Bản gốc đầy đủ của Đức: [`phu-luc-vinfast/02-deep-dive-report.md`](phu-luc-vinfast/02-deep-dive-report.md)
- Thử nghiệm Xanh SM (bài học Rule + LLM): [`phu-luc-xanhsm/`](phu-luc-xanhsm/02-deep-dive-report.md)
- Nhật ký dùng AI: [03-ai-log.md](03-ai-log.md)
