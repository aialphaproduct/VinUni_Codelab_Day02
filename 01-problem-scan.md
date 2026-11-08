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
**Phạm vi đóng góp:** Bản tổng hợp của nhóm trên `main`. Mỗi thành viên vẫn giữ bài Scan & Quick Cards cá nhân trên branch riêng để chấm điểm cá nhân (I1).

---

## 🏛️ Bối cảnh

Nhóm đóng vai trò **AI Product Engineer** tại **Vin Smart Future** (đơn vị công nghệ hợp nhất của Vingroup), có nhiệm vụ quét (scan) các điểm nghẽn vận hành tại các công ty thành viên và đề xuất giải pháp AI phù hợp.

---

## 🔍 Phase 1 — SCAN (4 Lenses) — đề tài thật của 6 thành viên

Mỗi thành viên tự scan và chọn một đề tài trên branch cá nhân; bảng dưới tổng hợp đề tài chính của từng người.

| # | Người đề xuất | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|---|
| 1 | Lưu Thanh Mỹ | **Xanh SM (GSM)** | Lặp lại | Tài xế báo hết pin giữa đường. Trạm sạc và số trụ trống **đã xem được trên app có sẵn**, nhưng điều phối viên vẫn phải **tự quyết chỉ đường hay điều xe sạc di động theo mức pin** và soạn tin hướng dẫn trong lúc bị hối thúc — lặp lại nhiều lần mỗi ca trực; quyết định sai thì xe cạn pin giữa đường hoặc tốn chi phí điều xe. |
| 2 | Lưu Văn Việt Đức | **VinFast — Dịch vụ hậu mãi** | Pain từ người khác | Khách mô tả hiện tượng của xe ngắn và thiếu thông tin (*"điều hòa không mát"*); cố vấn dịch vụ phải tự phát hiện mục còn thiếu (thời điểm, tần suất, điều kiện) và hỏi lại trước khi lập phiếu tiếp nhận. |
| 3 | Nguyễn Công Tĩnh | **Vinhomes – Vinpearl** | Pain từ người khác | Cư dân và chủ sở hữu BĐS nghỉ dưỡng phải liên hệ nhiều đầu mối (phí dịch vụ, pháp lý, vận hành, nghỉ dưỡng) mà không có một đầu mối chung; yêu cầu bị chuyển qua lại và phải trình bày lại nhiều lần. |
| 4 | Vũ Trí Dũng | **Vinmec** | Tốn thời gian | Kiểm tra, đối chiếu hồ sơ bảo hiểm y tế và xử lý yêu cầu bổ sung giấy tờ trước khi thanh toán; đối soát viện phí, mã dịch vụ và hóa đơn với hồ sơ điều trị. |
| 5 | Phạm Quang Trường | **Xanh SM (GSM)** | Tốn thời gian | Điều phối viên phải nghe lại ghi âm cuộc gọi hủy chuyến và đọc ghi chú tài xế để tổng hợp nguyên nhân hủy chuyến phổ biến, tìm pattern lỗi hệ thống. |
| 6 | Khổng Tiến Dương | **Vinhomes** | Lặp lại | Mỗi ngày ban quản lý nhận hàng trăm phản ánh cư dân qua App Vinhomes Resident (mất nước, hỏng đèn, thang máy, tiếng ồn…) và phải phân loại, điều hướng thủ công tới đúng bộ phận. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

> Số phút/lượt trong các card là **ước lượng ban đầu, chưa đo**. Card #2 và #3 lấy từ bài cá nhân của Đức và Tĩnh. Riêng Card #1 đã có số liệu đo trên bộ thử 24 ca (xem [02-deep-dive-report.md](02-deep-dive-report.md), mục 4).

### Quick Problem Card #1 — Xanh SM: Xử lý sự cố hết pin thực địa ⭐ (Được chọn cho Deep-Dive) *(đề xuất: Lưu Thanh Mỹ)*

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Tài xế Xanh SM báo hết pin/pin yếu giữa đường;    │
│ điều phối viên phải chọn chỉ đường tới trạm sạc hay điều xe │
│ sạc di động, rồi soạn tin hướng dẫn.                        │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau (Actor)? Điều phối viên (quá tải giờ cao điểm); │
│ tài xế (chờ đợi, rủi ro cạn pin giữa đường).                │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Nhận báo cáo ──> 2. Tra GPS xe ──> 3. Xem trạm trống   │
│   trên app có sẵn ──> 4. Chọn hành động + soạn tin ──>      │
│   5. Điều xe sạc di động nếu pin quá thấp                   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 4 (giả định ~5 phút,  │
│ chưa đo): dữ liệu trạm đã có trên app, cái khó là quyết định│
│ đúng theo mức pin. Sai ngưỡng → cạn pin hoặc tốn chi phí.   │
│ AI hỗ trợ ở bước nào? Bước 4: code đọc % pin và quyết ngưỡng│
│ < 5%, LLM soạn tin nháp và suy luận khi không có con số.    │
│                                                             │
│ Metric (đã đo trên 24 ca giả lập):                          │
│ • 100% ca pin < 5% được điều xe sạc — đạt 13/13             │
│ • Điều xe thừa ≤ 1/11 ca pin ≥ 5% — đạt 0/11 (hybrid)       │
│ • 100% tin có [DRAFT_ONLY], 0 lần lộ prompt — đạt           │
│ • Thời gian ~11–12 → dưới 3 phút/lượt (mục tiêu, chưa đo)   │
│                                                             │
│ Quick Architecture: [x] Rule + LLM (hybrid) + HITL           │
│ Boundary: không gửi tin khi chưa duyệt; pin < 5% không chỉ  │
│ đường tới trạm; lời tài xế không thay đổi được quy tắc.     │
└─────────────────────────────────────────────────────────────┘
```

### Quick Problem Card #2 — VinFast: Phát hiện thông tin còn thiếu trong mô tả sửa chữa *(đề xuất: Lưu Văn Việt Đức)*

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Mô tả của khách chưa đủ thông tin, cố vấn dịch vụ │
│ phải xác định nội dung còn thiếu và hỏi bổ sung trước khi   │
│ hoàn thiện phiếu tiếp nhận.                                 │
│ Công ty thành viên: [x] VinFast — Dịch vụ hậu mãi           │
│                                                             │
│ Ai đang đau (Actor)? Cố vấn dịch vụ; khách hàng phải trả    │
│ lời nhiều lượt.                                             │
│                                                             │
│ Workflow hiện tại (cần xác minh):                           │
│   1. Khách gửi mô tả ──> 2. Cố vấn đọc, kiểm tra ──>        │
│   3. Xác định thông tin thiếu ──> 4. Hỏi khách, ghi nhận ──>│
│   5. Hoàn thiện phiếu tiếp nhận                             │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3–4 (chưa đo)         │
│ AI hỗ trợ ở bước nào? Đối chiếu mô tả với checklist, liệt kê│
│ mục thiếu và đề xuất câu hỏi, không hỏi lại điều đã có.     │
│                                                             │
│ Metric: trên ≥ 20 ca giả lập, phát hiện đúng ≥ 90% mục thiếu│
│ (đã đo trên GPT-4o-mini: 65% — chưa đạt, xem phụ lục).      │
│                                                             │
│ Quick Architecture: [x] Rule + LLM + Human Review            │
│ Boundary: không tự điền, không chẩn đoán nguyên nhân hỏng.  │
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
│ phân loại và chuyển tiếp yêu cầu.                           │
│ AI hỗ trợ ở bước nào? Tiếp nhận qua một đầu mối, phân loại, │
│ đề xuất phòng ban phụ trách, lưu lịch sử trao đổi.          │
│                                                             │
│ Metric: phân loại & điều hướng đúng ≥ 90% trên 100 yêu cầu  │
│ thử; giảm ≥ 50% số lần phải cung cấp lại thông tin; 100%    │
│ yêu cầu có mã tiếp nhận và trạng thái theo dõi.             │
│                                                             │
│ Quick Architecture: [x] LLM (+ HITL cho quyết định quan     │
│ trọng). Boundary: không phê duyệt pháp lý, không quyết định │
│ phí dịch vụ, không cam kết quyền lợi.                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Quyết định lựa chọn của nhóm

Nhóm chọn **Card #1 — Xanh SM: Xử lý sự cố hết pin thực địa** để Deep-Dive (xem chi tiết tại [02-deep-dive-report.md](02-deep-dive-report.md)), vì:

- Tác động trực tiếp đến an toàn vận hành thời gian thực (xe cạn pin giữa đường), không thể trì hoãn như Card #2/#3.
- Ranh giới an toàn (Operational Boundary) rõ ràng, kiểm chứng được bằng bộ thử 24 ca: kiến trúc hybrid đạt 13/13 ca pin nguy cấp, 7/7 ca tấn công, 0 điều xe thừa.
- Khớp trực tiếp với ranh giới mà file code `prompt_prototype.py` của lab kiểm tra.
- **Card #2 (VinFast — Đức)** có phương pháp đánh giá tốt nhất nhóm, nhưng recall đo được mới đạt 65% (mục tiêu 90%), nên giữ làm bài đối chiếu ở [`phu-luc-vinfast/`](phu-luc-vinfast/02-deep-dive-report.md); phương pháp đánh giá của Đức được dùng lại cho bài chính.
- **Card #3 (Vinhomes – Vinpearl — Tĩnh)** giá trị trải nghiệm cao nhưng chưa có dữ liệu thử nghiệm, và phần định tuyến phòng ban có thể bắt đầu bằng Rule trước khi cần LLM.
- Các đề tài Vinmec (Dũng), hủy chuyến Xanh SM (Trường), phân loại khiếu nại Vinhomes (Dương): rủi ro y tế/compliance cao, là phân tích offline, hoặc giải được bằng Rule-based router trước — ưu tiên AI thấp hơn trong phạm vi lab.
