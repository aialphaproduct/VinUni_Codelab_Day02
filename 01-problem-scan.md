# 01 — Problem Scan & Quick Cards

**Tên nhóm:** Simple-Tech
**Thành viên tham gia:**
| # | Họ và tên | Email |
|---|-----------|-------|
| 1 | Lưu Thanh Mỹ (Trưởng nhóm) | data97688@gmail.com |
| 2 | Lưu Văn Việt Đức | luuvanvietduc@gmail.com |
| 3 | Nguyễn Công Tĩnh | tinh22102004@gmail.com |
| 4 | Vũ Trí Dũng | dungvutri25@gmail.com |
| 5 | Phạm Quang Trường | truongpham090325@gmail.com |
| 6 | Khổng Tiến Dương | khongtienduongcv@gmail.com |

**Người thực hiện nội dung gốc:** Lưu Thanh Mỹ
**Phạm vi đóng góp:** Bài Scan & Quick Cards **cá nhân** của Lưu Thanh Mỹ trên branch `luuthanhmy` (chấm điểm cá nhân I1), cùng nội dung với [bản nhóm trên main](https://github.com/aialphaproduct/VinUni_Codelab_Day02/blob/main/01-problem-scan.md). Đề tài cá nhân của Mỹ là Card #2 (Xanh SM), chi tiết ở [02-deep-dive-report.md](02-deep-dive-report.md).

---

## 🏛️ Bối cảnh

Nhóm đóng vai trò **AI Product Engineer** tại **Vin Smart Future** (đơn vị công nghệ hợp nhất của Vingroup), có nhiệm vụ quét (scan) các điểm nghẽn vận hành tại các công ty thành viên và đề xuất giải pháp AI phù hợp.

---

## 🔍 Phase 1 — SCAN (4 Lenses) — đề tài thật của 6 thành viên

Mỗi thành viên tự scan và chọn một đề tài trên branch cá nhân; bảng dưới tổng hợp đề tài chính của từng người.

| # | Người đề xuất | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|---|
| 1 | Lưu Thanh Mỹ | **Xanh SM (GSM)** | Pain từ người khác | Tài xế **tự tra trạm sạc trên app** và tự đi sạc, nhưng app không cho biết xe có chạy tới nơi nổi không khi pin rất thấp. Khi pin nguy cấp, tài xế phải gọi tổng đài; điều phối viên **tự quyết cho tài xế tự chạy tới trạm hay điều xe sạc di động** và soạn phản hồi trong lúc bị hối thúc — quyết định sai thì xe cạn pin giữa đường hoặc tốn chi phí điều xe. |
| 2 | Lưu Văn Việt Đức | **VinFast — Dịch vụ hậu mãi** | Pain từ người khác | Khách mô tả hiện tượng của xe ngắn và thiếu thông tin (*"điều hòa không mát"*); cố vấn dịch vụ phải tự phát hiện mục còn thiếu (thời điểm, tần suất, điều kiện) và hỏi lại trước khi lập phiếu tiếp nhận. |
| 3 | Nguyễn Công Tĩnh | **Vinhomes – Vinpearl** | Pain từ người khác | Cư dân và chủ sở hữu BĐS nghỉ dưỡng phải liên hệ nhiều đầu mối (phí dịch vụ, pháp lý, vận hành, nghỉ dưỡng) mà không có một đầu mối chung; yêu cầu bị chuyển qua lại và phải trình bày lại nhiều lần. |
| 4 | Vũ Trí Dũng | **Vinmec** | Tốn thời gian | Kiểm tra quyền lợi bảo hiểm (BHYT / bảo hiểm thương mại) và rà soát hồ sơ bảo lãnh viện phí trước khi thanh toán; hồ sơ thiếu giấy tờ khiến yêu cầu bảo lãnh bị trả về, bệnh nhân phải chờ. Deep-dive cá nhân: *Vinmec Prior-Auth & Eligibility Co-Pilot*. |
| 5 | Phạm Quang Trường | **Xanh SM (GSM)** | Tốn thời gian | Điều phối viên phải nghe lại ghi âm cuộc gọi hủy chuyến và đọc ghi chú tài xế để tổng hợp nguyên nhân hủy chuyến phổ biến, tìm pattern lỗi hệ thống. |
| 6 | Khổng Tiến Dương | **Vinhomes** | Lặp lại | Mỗi ngày ban quản lý nhận hàng trăm phản ánh cư dân qua App Vinhomes Resident (mất nước, hỏng đèn, thang máy, tiếng ồn…) và phải phân loại, điều hướng thủ công tới đúng bộ phận. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

> Số phút/lượt trong các card là **ước lượng ban đầu, chưa đo**. Mỗi card lấy từ bài cá nhân của người đề xuất. Card #1 và #2 đã có số liệu đo trên bộ thử (xem [02-deep-dive-report.md](https://github.com/aialphaproduct/VinUni_Codelab_Day02/blob/main/02-deep-dive-report.md) và [phụ lục Xanh SM](02-deep-dive-report.md)).

### Quick Problem Card #1 — VinFast: Hỏi đúng ngay từ lần đầu khi tiếp nhận sửa chữa ⭐ (Được chọn cho Deep-Dive) *(đề xuất: Lưu Văn Việt Đức)*

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Mô tả của khách chưa đủ thông tin, cố vấn dịch vụ │
│ phải xác định nội dung còn thiếu và hỏi bổ sung trước khi   │
│ hoàn thiện phiếu tiếp nhận.                                 │
│ Công ty thành viên: [x] VinFast — Dịch vụ hậu mãi           │
│                                                             │
│ Ai đang đau (Actor)? Cố vấn dịch vụ; khách hàng phải trả    │
│ lời nhiều lượt.                                             │
│                                                             │
│ Workflow thủ công hiện tại (5 bước, cần xác minh):          │
│   1. Khách gửi mô tả ──> 2. Cố vấn đọc, kiểm tra ──>        │
│   3. Xác định thông tin thiếu ──> 4. Hỏi khách, ghi nhận ──>│
│   5. Hoàn thiện phiếu tiếp nhận                             │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3–4 (⏱ ~4–7 phút/lượt,│
│ ước lượng, chưa đo)                                         │
│ AI hỗ trợ ở bước nào? Đối chiếu mô tả với checklist, liệt kê│
│ mục thiếu và đề xuất câu hỏi, không hỏi lại điều đã có.     │
│                                                             │
│ Metric: trên ≥ 20 ca giả lập, phát hiện đúng ≥ 90% mục thiếu│
│ (đã đo GPT-4o-mini: 65%; lớp Rule bắt thêm 15/21 lỗi).      │
│                                                             │
│ Quick Architecture: [ ] No AI  [x] Rule  [x] LLM  [ ] Agent │
│ (Rule + LLM, cố vấn duyệt mọi bản nháp — HITL)              │
│ Boundary: không tự điền, không chẩn đoán nguyên nhân hỏng.  │
└─────────────────────────────────────────────────────────────┘
```

### Quick Problem Card #2 — Xanh SM: Ca tài xế báo pin nguy cấp *(đề xuất: Lưu Thanh Mỹ — thử nghiệm ở [02-deep-dive-report.md](02-deep-dive-report.md))*

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Tài xế tự tra trạm sạc trên app, nhưng khi pin    │
│ nguy cấp phải gọi tổng đài; điều phối viên phải quyết cho   │
│ tài xế tự chạy tới trạm hay điều xe sạc di động.            │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau (Actor)? Điều phối viên (quyết định dưới áp lực │
│ giờ cao điểm); tài xế (rủi ro cạn pin giữa đường).          │
│                                                             │
│ Workflow hiện tại (ca leo thang, 4 bước):                   │
│   1. Tài xế gọi/nhắn báo pin nguy cấp ──> 2. Xác minh mức   │
│   pin, vị trí, khoảng cách trạm ──> 3. Quyết định tự chạy   │
│   hay điều xe + soạn phản hồi ──> 4. Điều xe sạc nếu cần    │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (giả định ~5 phút,  │
│ chưa đo). App không đánh giá được xe có tới nơi được không; │
│ sai ngưỡng → cạn pin giữa đường hoặc tốn chi phí điều xe.   │
│ AI hỗ trợ ở bước nào? Bước 3: code đọc % pin và quyết ngưỡng│
│ < 5%, LLM soạn phản hồi và suy luận khi không có con số.    │
│                                                             │
│ Metric (đã đo trên 24 ca giả lập):                          │
│ • 100% ca pin < 5% được điều xe sạc — đạt 13/13             │
│ • Điều xe thừa ≤ 1/11 ca pin ≥ 5% — đạt 0/11 (hybrid)       │
│ • 100% tin có [DRAFT_ONLY], 0 lần lộ prompt — đạt           │
│ • Thời gian ca leo thang ~10 → dưới 3 phút (mục tiêu)       │
│                                                             │
│ Quick Architecture: [ ] No AI  [x] Rule  [x] LLM  [ ] Agent │
│ (hybrid: code quyết ngưỡng pin, LLM soạn tin — HITL)        │
│ Boundary: không gửi tin khi chưa duyệt; pin < 5% không chỉ  │
│ đường tới trạm; lời tài xế không thay đổi được quy tắc.     │
└─────────────────────────────────────────────────────────────┘
```

### Quick Problem Card #3 — Vinhomes – Vinpearl: Một đầu mối hỗ trợ cư dân/chủ sở hữu BĐS *(đề xuất: Nguyễn Công Tĩnh)*

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Cư dân và chủ sở hữu BĐS nghỉ dưỡng phải liên hệ  │
│ nhiều phòng ban Vinhomes/Vinpearl (phí dịch vụ, pháp lý,    │
│ vận hành, nghỉ dưỡng) mà không có đầu mối chung.            │
│ Công ty thành viên: [x] Vinhomes  [x] Vinpearl              │
│                                                             │
│ Ai đang đau (Actor)? Cư dân/chủ sở hữu (trình bày lại nhiều │
│ lần), CSKH (thiếu lịch sử yêu cầu), ban quản lý (chuyển     │
│ tiếp nhiều lần).                                            │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Phát sinh nhu cầu ──> 2. Tự tìm kênh liên hệ ──>       │
│   3. Trình bày với bộ phận đầu tiên ──> 4. Bị chuyển phòng  │
│   ban, kể lại từ đầu ──> 5. Liên hệ lại để hỏi tiến độ      │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2–4: xác định đầu mối,│
│ phân loại, chuyển tiếp (⏱ chưa đo phút/lượt).               │
│ AI hỗ trợ ở bước nào? Tiếp nhận qua một đầu mối, phân loại, │
│ đề xuất phòng ban phụ trách, lưu lịch sử trao đổi.          │
│                                                             │
│ Metric: phân loại & điều hướng đúng ≥ 90% trên 100 yêu cầu  │
│ thử; giảm ≥ 50% số lần phải cung cấp lại thông tin; 100%    │
│ yêu cầu có mã tiếp nhận và trạng thái theo dõi.             │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
│ (+ HITL cho quyết định quan trọng). Boundary: không phê     │
│ duyệt pháp lý, không quyết định phí, không cam kết quyền lợi│
└─────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Quyết định lựa chọn của nhóm

Nhóm chọn **Card #1 — VinFast: Hỏi đúng ngay từ lần đầu** để Deep-Dive (xem [02-deep-dive-report.md](https://github.com/aialphaproduct/VinUni_Codelab_Day02/blob/main/02-deep-dive-report.md)), vì đây là đề tài duy nhất hội đủ bốn điều kiện:

- **Nỗi đau có thật, chưa được giải quyết:** biểu mẫu đặt lịch nhận mô tả tự do nhưng không biết mô tả đã đủ để chẩn đoán chưa; phiếu thiếu thông tin làm giảm tỉ lệ sửa đúng ngay lần đầu.
- **Thật sự cần LLM:** khách mô tả bằng tiếng Việt đời thường ("kêu cụp cụp", "máy lạnh yếu") — Rule không đọc hiểu được.
- **Đo được:** 20 ca giả lập kèm đáp án, đã chạy trên Gemini và GPT-4o-mini; lỗi được phân loại đủ rõ để có lộ trình cải thiện cụ thể.
- **Ranh giới rõ:** không chẩn đoán, không báo giá, không tự điền điều khách chưa nói — giữ vững ở cả 3 ca tấn công.

Các đề tài còn lại:

- **Card #2 (Xanh SM — Mỹ):** nhóm đã đo 24 ca và 4 lượt, nhưng tài xế đã tự tra trạm sạc trên app nên phạm vi bài toán hẹp. Giữ làm [phụ lục](02-deep-dive-report.md) vì đem lại bài học kiến trúc "quyết định tất định để code làm".
- **Card #3 (Vinhomes – Vinpearl — Tĩnh):** giá trị trải nghiệm cao nhưng phạm vi rộng và chưa có dữ liệu thử nghiệm.
- **Vinmec (Dũng), hủy chuyến Xanh SM (Trường), phân loại khiếu nại Vinhomes (Dương):** rủi ro y tế/compliance cao, là phân tích offline, hoặc giải được bằng Rule-based router trước — ưu tiên AI thấp hơn trong phạm vi lab.
