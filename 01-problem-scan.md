# Lab 02 — Problem Scan & Quick Problem Cards (Vin Smart Future)

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

> **Họ và tên / Branch:** Vũ Trí Dũng (`VuTriDung`)  
> **Vai trò:** AI Product Engineer — **Vin Smart Future (Vingroup)**  
> **Mảng khảo sát trọng tâm:** **Hệ thống Y tế Hàn lâm Vinmec**

---

## 🏛️ Bối cảnh khảo sát

Trong vai trò là **AI Product Engineer** tại **Vin Smart Future**, em tập trung rà soát các điểm nghẽn vận hành (operational bottlenecks) tại **Hệ thống Y tế Vinmec** — nơi đội ngũ bác sĩ, điều dưỡng, nhân viên bảo lãnh viện phí và kế toán đang phải xử lý khối lượng lớn hồ sơ y khoa bán cấu trúc/phi cấu trúc mỗi ngày. Mục tiêu là nhận diện đúng bài toán thực tế, định lượng tổn thất bằng số liệu benchmark ngành y tế đáng tin cậy và chọn đúng kiến trúc kỹ thuật (**Rule-based** hay **LLM Feature**) trước khi bắt tay xây dựng nguyên mẫu.

---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội vận hành (Cá nhân)

Sử dụng **4 Lenses** (_Repetitive, Time-consuming, AI-upgrade, Stakeholder Pain_) để quét qua chuỗi vận hành khám chữa bệnh và thanh toán bảo hiểm tại **Vinmec**:

|  #  | Subsidiary | Lens                                              | Mô tả ngắn bài toán                                                                                                                                                          |
| :-: | :--------- | :------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  1  | **Vinmec** | **Repetitive** _(Lặp lại)_                        | Nhập liệu và chuẩn hóa hồ sơ bệnh án từ nhiều loại giấy tờ chuyển tuyến, kết quả xét nghiệm ngoại viện và biểu mẫu khác nhau vào hệ thống HIS/EMR.                           |
|  2  | **Vinmec** | **Time-consuming** _(Tốn thời gian)_              | Kiểm tra, đối chiếu quyền lợi hồ sơ bảo hiểm y tế / bảo hiểm thương mại và xử lý các yêu cầu bổ sung giấy tờ (_prior authorization_) trước khi thanh toán bảo lãnh viện phí. |
|  3  | **Vinmec** | **AI-upgrade** _(AI có thể tốt hơn)_              | Tối ưu quy trình đặt lịch khám, phân luồng chuyên khoa ban đầu, nhắc lịch thông minh và tự động sắp xếp lại slot khám khi bệnh nhân hủy hoặc không đến (_no-show_).          |
|  4  | **Vinmec** | **Repetitive** _(Lặp lại)_                        | Đối soát viện phí, mã dịch vụ kỹ thuật, vật tư tiêu hao và hóa đơn giữa hồ sơ chỉ định điều trị lâm sàng với hệ thống thanh toán kế toán.                                    |
|  5  | **Vinmec** | **Stakeholder Pain** _(Pain từ người trong cuộc)_ | Bác sĩ mất quá nhiều thời gian gõ máy nhập liệu, tổng hợp triệu chứng và hoàn thiện báo cáo khám chữa bệnh trên EMR thay vì tập trung thăm khám, tư vấn cho bệnh nhân.       |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Từ 5 bài toán trên, em chọn ra **3 bài toán gây thất thoát thời gian và áp lực vận hành lớn nhất** để đánh giá nhanh kiến trúc và thước đo thành công:

- **Card #1 (Problem #2):** Kiểm tra quyền lợi và đối chiếu hồ sơ bảo lãnh viện phí (_Insurance Eligibility & Prior Authorization_).
- **Card #2 (Problem #4):** Đối soát viện phí, mã dịch vụ và hóa đơn (_Medical Billing & Claim Reconciliation_).
- **Card #3 (Problem #5):** Hỗ trợ bác sĩ soạn thảo và hoàn thiện ghi chú khám chữa bệnh (_AI Clinical Documentation Assistant_).

---

## 1. Quick Problem Card #1 — Kiểm tra và đối chiếu hồ sơ bảo hiểm (Problem #2)

<!-- prettier-ignore-start -->
```text
┌──────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                │
│                                                                      │
│ Bài toán (1 câu):                                                    │
│ Tự động kiểm tra quyền lợi bảo hiểm và phát hiện hồ sơ thiếu giấy tờ │
│ trước khi gửi yêu cầu phê duyệt thanh toán bảo lãnh viện phí.        │
│                                                                      │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes           │
│                     [x] Vinmec   [ ] Khác: __________                │
│                                                                      │
│ Ai đang đau (Actor)?                                                 │
│ Chuyên viên bảo lãnh viện phí, nhân viên tiếp nhận & thu ngân,       │
│ và bệnh nhân đang chờ duyệt bảo lãnh tại viện.                       │
│                                                                      │
│ Workflow thủ công hiện tại (5 bước):                                 │
│ 1. Tiếp nhận yêu cầu & thẻ BH --> 2. Kiểm tra quyền lợi hợp đồng PDF │
│ --> 3. Đối chiếu mã ICD-10 & dịch vụ --> 4. Kiểm tra đủ giấy tờ      │
│ --> 5. Soạn giải trình & gửi cổng bảo hiểm duyệt                     │
│                                                                      │
│ Bước nào tốn thời gian/lỗi nhất?                                     │
│ Bước 2–4: Kiểm tra điều khoản loại trừ & xử lý prior authorization   │
│ (⏱ Benchmark: 24 phút/giao dịch thủ công — CAQH 2024)                │
│                                                                      │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                │
│ OCR trích xuất chứng từ, LLM (RAG) đọc điều khoản hợp đồng bảo hiểm  │
│ để đối chiếu với chỉ định lâm sàng, cảnh báo thiếu giấy tờ & draft.  │
│                                                                      │
│ Đo thành công bằng gì (Metric có số)?                                │
│ - Giảm thời gian xử lý hồ sơ từ 24 phút ──> dưới 6 phút/lượt         │
│   (vượt mốc chuẩn điện tử hóa 10 phút của CAQH 2024).                │
│ - Phát hiện >= 95% hồ sơ thiếu chứng từ trước khi gửi duyệt, giảm    │
│   tỷ lệ từ chối/yêu cầu bổ sung lần đầu từ ~11,6% xuống < 4%.        │
│                                                                      │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent          │
└──────────────────────────────────────────────────────────────────────┘
```
<!-- prettier-ignore-end -->

**Nguồn trích dẫn thực증 (CAQH 2024 Index & Khảo sát AMA 2024):**

- **CAQH 2024 Index:** Kiểm tra quyền lợi bảo hiểm (_eligibility & benefit verification_) mất trung bình **16 phút** khi làm thủ công so với **4 phút** khi xử lý điện tử; xử lý phê duyệt trước (_prior authorization_) mất trung bình **24 phút** thủ công so với **10 phút** điện tử.
- **AMA 2024 Prior Authorization Survey:** Bác sĩ và nhân viên y tế mất trung bình **13 giờ mỗi tuần** chỉ để xử lý thủ tục _prior authorization_ (trung bình **39 yêu cầu/bác sĩ/tuần**).

---

## 2. Quick Problem Card #2 — Đối soát viện phí, mã dịch vụ và hóa đơn (Problem #4)

<!-- prettier-ignore-start -->
```text
┌──────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                │
│                                                                      │
│ Bài toán (1 câu):                                                    │
│ Tự động phát hiện sai lệch giữa chỉ định điều trị trên EMR, dịch vụ  │
│ thực tế đã thực hiện, mã dịch vụ kỹ thuật và hóa đơn viện phí.       │
│                                                                      │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes           │
│                     [x] Vinmec   [ ] Khác: __________                │
│                                                                      │
│ Ai đang đau (Actor)?                                                 │
│ Nhân viên kế toán viện phí, bộ phận thanh toán bảo hiểm & tài chính. │
│                                                                      │
│ Workflow thủ công hiện tại (5 bước):                                 │
│ 1. Thu thập log dịch vụ --> 2. Đối chiếu chỉ định bác sĩ trên HIS    │
│ --> 3. Kiểm tra mã dịch vụ & đơn giá --> 4. Đối chiếu hóa đơn ERP    │
│ --> 5. Phát hiện & xử lý sai lệch trước khi chốt thanh toán          │
│                                                                      │
│ Bước nào tốn thời gian/lỗi nhất?                                     │
│ Bước 3–5: Đối chiếu chéo dữ liệu và xử lý sai lệch giữa các hệ thống │
│ (⏱ Benchmark: 12 phút/claim submission thủ công — CAQH 2024)         │
│                                                                      │
│ Hệ thống tự động nhảy vào hỗ trợ ở bước nào?                         │
│ Rule Engine tự động khớp nối bảng dữ liệu HIS – ERP, gắn cờ các dòng │
│ lệch mã dịch vụ, số lượng vật tư hoặc đơn giá bất thường.            │
│                                                                      │
│ Đo thành công bằng gì (Metric có số)?                                │
│ - Giảm thời gian đối soát trước gửi claim từ 12 phút ──> dưới 2 phút │
│ - Giảm tỷ lệ từ chối thanh toán ban đầu (Initial Claim Denial Rate)  │
│   từ mức nền tham khảo 11,6% (Kodiak 2025) xuống dưới 3%.            │
│                                                                      │
│ Quick Architecture: [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent          │
└──────────────────────────────────────────────────────────────────────┘
```
<!-- prettier-ignore-end -->

**Nguồn trích dẫn thực chứng (CAQH 2024 Index & Kodiak Solutions 2025 Revenue Cycle Benchmark):**

- **CAQH 2024 Index:** Gửi yêu cầu thanh toán (_claim submission_) mất **12 phút** thủ công so với **5 phút** điện tử; tra cứu trạng thái thanh toán mất **25 phút** thủ công so với **7 phút** điện tử.
- **Kodiak Solutions (2025):** Tỷ lệ _Initial Claim Denial Rate_ trung bình trên bộ dữ liệu 2.300 bệnh viện năm 2025 đạt **11,6%** (tăng từ 11,4% năm 2024). Bài toán này ưu tiên **Rule-based Engine** thay vì LLM vì dữ liệu đầu vào là bảng số liệu có cấu trúc, đòi hỏi độ chính xác số học tuyệt đối 100%.

---

## 3. Quick Problem Card #3 — Soạn thảo và hoàn thiện hồ sơ khám chữa bệnh (Problem #5)

<!-- prettier-ignore-start -->
```text
┌──────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                │
│                                                                      │
│ Bài toán (1 câu):                                                    │
│ Hỗ trợ bác sĩ chuyển nội dung trao đổi lâm sàng và thông tin khám    │
│ bệnh thành bản ghi chú bệnh án có cấu trúc (SOAP) để giảm nhập liệu. │
│                                                                      │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes           │
│                     [x] Vinmec   [ ] Khác: __________                │
│                                                                      │
│ Ai đang đau (Actor)?                                                 │
│ Bác sĩ khám chữa bệnh, điều dưỡng phụ khám và bộ phận quản lý hồ sơ. │
│                                                                      │
│ Workflow thủ công hiện tại (5 bước):                                 │
│ 1. Tiếp nhận bệnh nhân --> 2. Khai thác triệu chứng & tiền sử bệnh   │
│ --> 3. Gõ nhập dữ liệu thô --> 4. Soạn ghi chú bệnh án chuẩn trên EMR│
│ --> 5. Bác sĩ rà soát & ký xác nhận hồ sơ                            │
│                                                                      │
│ Bước nào tốn thời gian/lỗi nhất?                                     │
│ Bước 3–4: Nhập liệu và tổng hợp thông tin vào hồ sơ bệnh án điện tử  │
│ (⏱ Benchmark: 10,3 phút/lượt khám — JAMA Network Open 2025)          │
│                                                                      │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                │
│ Speech-to-Text chuyển giọng nói thành văn bản y khoa, LLM tóm tắt và │
│ điền nháp vào biểu mẫu bệnh án có cấu trúc để bác sĩ kiểm duyệt.     │
│                                                                      │
│ Đo thành công bằng gì (Metric có số)?                                │
│ - Giảm thời gian ghi chú mỗi ca khám từ 10,3 ──> <= 8,2 phút (-20,4%)│
│ - Giảm 30% thời gian bác sĩ phải làm hồ sơ ngoài giờ (từ 50,6 xuống  │
│   35,4 phút/ngày) và giữ tỷ lệ câu phải sửa tay < 15%.               │
│                                                                      │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent          │
└──────────────────────────────────────────────────────────────────────┘
```
<!-- prettier-ignore-end -->

**Nguồn trích dẫn thực chứng (JAMA Network Open, 2025):**

- Nghiên cứu thực nghiệm lâm sàng trên 46 nhân viên y tế thuộc 17 chuyên khoa khi triển khai công cụ _AI Ambient Scribe_ ghi nhận:
  - Thời gian hoàn thiện ghi chú mỗi lượt khám giảm từ **10,3 phút xuống 8,2 phút** (giảm **20,4%**).
  - Thời gian làm hồ sơ ngoài giờ hành chính (_after-hours EHR "pajama time"_) giảm từ **50,6 phút xuống 35,4 phút/ngày** (giảm **30,0%**).
