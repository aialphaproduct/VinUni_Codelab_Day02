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

## 🔍 Phase 1 — SCAN (4 Lenses)

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|----------------------|
| 1 | **Xanh SM (GSM)** | Lặp lại | Khi tài xế báo hết pin giữa đường, điều phối viên phải thủ công tra cứu vị trí GPS, tìm trạm sạc VinFast còn trụ trống phù hợp loại cổng sạc, rồi soạn tin nhắn chỉ dẫn — lặp lại hàng chục lần mỗi ca trực. |
| 2 | **VinFast** | Lặp lại | Đối chiếu hóa đơn sạc điện hằng tuần từ hàng nghìn trụ sạc đối tác ngoài hệ thống với số liệu ghi nhận nội bộ, hiện làm thủ công trên Excel. |
| 3 | **Vinhomes** | AI có thể tốt hơn | Khiếu nại cư dân gửi qua App Vinhomes Resident (mất nước, hỏng thang máy, tiếng ồn...) đang được nhân viên tổng đài đọc và phân loại thủ công rồi mới chuyển đúng ban quản lý tòa nhà, phản hồi rập khuôn và chậm. |
| 4 | **Vinmec** | Pain từ người khác | Bác sĩ phàn nàn mất 20-30 phút/bệnh nhân để soạn tóm tắt hồ sơ xuất viện từ bệnh án điện tử, xét nghiệm và ghi chú lâm sàng. |
| 5 | **Xanh SM (GSM)** | Pain từ người khác | Điều phối viên phải nghe lại ghi âm cuộc gọi hủy chuyến và đọc ghi chú tài xế thủ công để tổng hợp nguyên nhân hủy chuyến phổ biến, dùng để báo cáo tuần cho vận hành. |

> **Ghi chú:** Sau khi thảo luận nhóm, cả nhóm thống nhất chọn bài toán **#1 — Xanh SM xử lý sự cố pin thực địa** để Deep-Dive, vì đây là tác vụ vận hành thời gian thực (real-time), ảnh hưởng trực tiếp đến an toàn tài xế và hiệu suất đội xe, đồng thời khớp với bài tập lập trình Prompt Prototype (Phase 4) của Lab.

---

## 👥 Scan của cả nhóm (đề tài cá nhân từng thành viên)

| Thành viên | Subsidiary | Đề tài cá nhân | Lens |
|---|---|---|---|
| Lưu Thanh Mỹ | Xanh SM | Co-pilot xử lý sự cố hết pin thực địa | Lặp lại / Stakeholder pain |
| Lưu Văn Việt Đức | VinFast | Chuẩn hóa mô tả sửa chữa thành phiếu tiếp nhận ([phụ lục](phu-luc-vinfast/01-problem-scan.md)) | Stakeholder pain |
| Nguyễn Công Tĩnh | Vinhomes – Vinpearl | Tiếp nhận yêu cầu cư dân/chủ sở hữu BĐS nghỉ dưỡng qua một đầu mối | AI-upgrade |
| Vũ Trí Dũng | Vinmec | Đối chiếu hồ sơ bảo hiểm y tế; đối soát viện phí, mã dịch vụ, hóa đơn | Tốn thời gian / Lặp lại |
| Phạm Quang Trường | Xanh SM | Phân tích lý do hủy chuyến từ ghi âm + ghi chú tài xế | Stakeholder pain |
| Khổng Tiến Dương | Vinhomes | Phân loại & điều hướng khiếu nại cư dân | Lặp lại |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

> Số phút/lượt trong các card là **ước lượng ban đầu, chưa đo**. Riêng Card #1 đã có số liệu đo trên bộ thử 24 ca (xem [02-deep-dive-report.md](02-deep-dive-report.md), mục 4).

### Quick Problem Card #1 — Xanh SM: Xử lý sự cố hết pin thực địa ⭐ (Được chọn cho Deep-Dive)

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                               │
│ Bài toán: Tài xế Xanh SM báo hết pin/pin yếu giữa đường,     │
│ cần điều phối viên tra cứu trạm sạc hoặc điều xe cứu hộ.     │
│ Công ty thành viên: [x] Xanh SM (GSM)                        │
│                                                               │
│ Ai đang đau (Actor)? Điều phối viên (quá tải giờ cao điểm),  │
│ Tài xế (chờ đợi, rủi ro kẹt xe giữa đường vì cạn pin).        │
│                                                               │
│ Workflow thủ công hiện tại (5 bước):                          │
│   1. Nhận cuộc gọi sự cố ──> 2. Tra GPS xe ──>                │
│   3. Tra trạm sạc trống ──> 4. Soạn tin chỉ dẫn ──>           │
│   5. Gọi xe cứu hộ nếu cần                                    │
│                                                               │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3-4 (⏱ ~10 phút/lượt)   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4                │
│ (tự động lấy vị trí, lọc trạm sạc phù hợp, draft tin nhắn)    │
│                                                               │
│ Đo thành công bằng gì (Metric có số)?                         │
│ • 100% ca pin < 5% được điều xe sạc (đã đo: 13/13)            │
│ • Điều xe thừa ≤ 1/11 ca pin ≥ 5% (đã đo: 0/11 với hybrid)    │
│ • Thời gian ~15 phút ──> dưới 3 phút/lượt (giả định, chưa đo) │
│                                                               │
│ Quick Architecture: [x] Rule + LLM (hybrid) — cập nhật sau    │
│ khi đo: LLM thuần lẫn ngưỡng số, xem 02-deep-dive mục 4.3     │
└─────────────────────────────────────────────────────────────┘
```

### Quick Problem Card #2 — Vinhomes: Phân loại & điều hướng phản ánh cư dân

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                        │
│                                                                │
│ Bài toán: Khiếu nại/phản ánh cư dân gửi qua App Vinhomes      │
│ Resident cần được phân loại đúng hạng mục và chuyển đúng ban  │
│ quản lý tòa nhà phụ trách.                                    │
│ Công ty thành viên: [x] Vinhomes                              │
│                                                                │
│ Ai đang đau (Actor)? Nhân viên tổng đài CSKH Vinhomes.        │
│                                                                │
│ Workflow thủ công hiện tại (4 bước):                          │
│   1. Đọc nội dung phản ánh ──> 2. Tra cứu tòa nhà/căn hộ ──>  │
│   3. Phân loại hạng mục (điện/nước/an ninh...) ──>            │
│   4. Chuyển ticket cho đúng ban quản lý                       │
│                                                                │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (phân loại sai hạng   │
│ mục dẫn đến chuyển nhầm ban, phải làm lại) (⏱ ~8 phút/lượt)   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3                │
│                                                                │
│ Đo thành công bằng gì (Metric có số)?                         │
│ Giảm thời gian phân loại + chuyển ticket từ 12 phút ──>       │
│ dưới 2 phút; độ chính xác phân loại ≥ 95%.                    │
│                                                                │
│ Quick Architecture: [x] Rule + LLM Feature (hybrid)            │
└─────────────────────────────────────────────────────────────┘
```

### Quick Problem Card #3 — Vinmec: Soạn tóm tắt hồ sơ xuất viện

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                        │
│                                                                │
│ Bài toán: Bác sĩ phải tự soạn bản tóm tắt xuất viện bằng tay  │
│ từ bệnh án điện tử, kết quả xét nghiệm và ghi chú lâm sàng.   │
│ Công ty thành viên: [x] Vinmec                                │
│                                                                │
│ Ai đang đau (Actor)? Bác sĩ điều trị / Điều dưỡng trưởng khoa.│
│                                                                │
│ Workflow thủ công hiện tại (4 bước):                          │
│   1. Mở bệnh án điện tử ──> 2. Đọc xét nghiệm + ghi chú ──>   │
│   3. Soạn bản tóm tắt bằng ngôn ngữ dễ hiểu ──>               │
│   4. Bác sĩ trưởng khoa duyệt trước khi phát cho bệnh nhân    │
│                                                                │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (⏱ 20-30 phút/ca)     │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 (draft bản tóm   │
│ tắt, bác sĩ chỉ cần rà soát & ký duyệt)                        │
│                                                                │
│ Đo thành công bằng gì (Metric có số)?                         │
│ Giảm thời gian soạn thảo từ 25 phút ──> dưới 8 phút/ca, vẫn   │
│ giữ nguyên bước bác sĩ duyệt 100% trước khi phát hành.        │
│                                                                │
│ Quick Architecture: [x] LLM Feature (bắt buộc HITL do y tế)    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Quyết định lựa chọn của nhóm

Nhóm chọn **Card #1 — Xanh SM: Xử lý sự cố hết pin thực địa** để Deep-Dive (xem chi tiết tại [02-deep-dive-report.md](02-deep-dive-report.md)), vì:

- Tác động trực tiếp đến an toàn vận hành thời gian thực, không thể trì hoãn xử lý như Card #2/#3.
- Ranh giới an toàn (Operational Boundary) rõ ràng, kiểm chứng được bằng bộ thử 24 ca: kiến trúc hybrid đạt 13/13 ca pin nguy cấp, 7/7 ca tấn công, 0 điều xe thừa.
- Khớp trực tiếp với ranh giới mà file code `prompt_prototype.py` của lab kiểm tra.
- Card #3 (Vinmec) tuy giá trị cao nhưng rủi ro y tế đòi hỏi quy trình compliance phức tạp hơn nhiều, cần một lab riêng để xử lý đúng mức.
- Card #2 (Vinhomes) có thể giải quyết tốt bằng rule-based router đơn giản trước khi cần đến LLM, độ ưu tiên AI thấp hơn.
