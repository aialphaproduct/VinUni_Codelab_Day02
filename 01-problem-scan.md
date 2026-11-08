# 01-problem-scan.md — Ý tưởng cá nhân & Nhóm (Vin Smart Future)

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

> **Học viên:** Nguyễn Công Tĩnh · **Branch cá nhân:**congtinhx  · **Lab 02: AI Product Scoping**
>
> Tài liệu này gồm **Phase 1 (SCAN)** và **Phase 2 (QUICK-ASSESS)** — 2 nội dung cá nhân bắt buộc, chấm theo Gate **I1. Scan & Cards (15 điểm)** trong `01-worksheet.md`.

---

## 🏛️ Bối cảnh: Tôi là ai?

Tôi là học viên đóng vai **AI Product Engineer tại Vin Smart Future** — đơn vị công nghệ thống nhất của Vingroup, nhiệm vụ xây dựng giải pháp AI / số hóa / tự động hóa xuyên suốt các công ty thành viên (VinFast, Xanh SM, Vinhomes, Vinmec, Vinpearl/VinWonders).

---

# 🔍 Phase 1 — SCAN: Danh sách bài toán cá nhân

Sử dụng **4 Lenses** (Lặp lại / Tốn thời gian / AI có thể tốt hơn / Pain từ người khác) quét qua vận hành của các công ty thành viên Vingroup — theo yêu cầu *"Ghi lại ít nhất 5 bài toán/bottleneck thực tế"* trong worksheet:

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Vinhomes** | Pain từ người khác | Cầu nối hợp nhất cư dân ↔ Vingroup: Cư dân và chủ sở hữu bất động sản nghỉ dưỡng phải liên hệ riêng lẻ nhiều đầu mối như Ban quản lý phí dịch vụ, bộ phận pháp lý Vinhomes, dịch vụ nghỉ dưỡng Vinpearl... nhưng không có đầu mối hỗ trợ chung. Điều này khiến cư dân mất thời gian, phải lặp lại thông tin nhiều lần mỗi khi chuyển phòng ban và khó theo dõi tiến độ xử lý yêu cầu. |
| 2 | **Vinhomes** | AI có thể tốt hơn | CSKH/BQL trả lời cư dân rập khuôn, chậm (vài tiếng đến hơn 1 ngày); chất lượng trả lời không nhất quán giữa các tòa dù cùng hệ thống App. |
| 3 | **VinFast** | Lặp lại | So khớp hóa đơn sạc điện hằng tuần từ hàng nghìn trụ sạc đối tác ngoài với số liệu hệ thống tài chính — khối lượng lặp lại lớn, dễ sai sót do đối chiếu tay. |
| 4 | **Xanh SM** | Pain từ người khác | Tài xế phàn nàn hệ thống gợi ý điểm đón khách không chính xác; phản hồi của tài xế bị điều vận xử lý thủ công từng cuốc qua tổng đài. |
| 5 | **Vinmec** | Tốn thời gian | Bác sĩ soạn tóm tắt hồ sơ xuất viện (Discharge Summary) thủ công ~20–30 phút/bệnh nhân, gây quá tải trong khi hồ sơ là bắt buộc để ra viện. |
| 6 | **Vinpearl** | Pain từ người khác | Phàn nàn khẩn cấp trong review khách sạn ("phòng bẩn", "nhân viên thái độ tệ") bị trôi giữa hàng nghìn review trên Booking/Agoda/Google Maps, đến Manager chậm hoặc không được lọc đúng mức độ. |

*(Danh sách khởi điểm có tham khảo các gợi ý trong `03-inspiration-kit.md`, sau đó tự lọc lại theo lens riêng của từng bài.)*

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn top 3 bài toán từ bảng SCAN để hoàn thiện Quick Problem Cards: **#1 (Vinhomes), #3 (VinFast), #5 (Vinmec)**.

## Card #1 — Vinhomes: Tiếp nhận và xử lý yêu cầu hỗ trợ cư dân/chủ sở hữu BĐS nghỉ dưỡng thuộc hệ sinh thái Vinhomes – Vinpearl. 🔥 TOP PICK

```text
┌──────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                         │
│                                                              │
│ Bài toán (1 câu): Cư dân và chủ sở hữu BĐS nghỉ dưỡng         │
│ phải liên hệ nhiều phòng ban khác nhau của Vinhomes và       │
│ Vinpearl để giải quyết các vấn đề về phí dịch vụ, pháp lý,   │
│ vận hành và nghỉ dưỡng nhưng chưa có một đầu mối hỗ trợ      │
│ chung, khiến thông tin bị phân tán và xử lý kéo dài.         │
│                                                              │
│ Công ty thành viên: [x] Vinhomes  [x] Vinpearl               │
│                                                              │
│ Ai đang đau (Actor)?                                         │
│ - Cư dân/chủ sở hữu BĐS: Phải liên hệ nhiều đầu mối,          │
│   mất thời gian và phải cung cấp lại thông tin nhiều lần.    │
│ - Bộ phận CSKH: Khó theo dõi toàn bộ lịch sử yêu cầu         │
│   khi thông tin nằm ở nhiều phòng ban.                       │
│ - Ban quản lý: Mất thời gian xác định đúng đơn vị             │
│   chịu trách nhiệm và chuyển tiếp yêu cầu.                   │
│ - Bộ phận Vinhomes/Vinpearl: Tiếp nhận yêu cầu không          │
│   đúng phạm vi chuyên môn, phải chuyển tiếp nhiều lần.       │
│                                                              │
│ Workflow thủ công hiện tại (5 bước):                         │
│ 1. Cư dân phát sinh nhu cầu hoặc vấn đề cần hỗ trợ.          │
│ 2. Cư dân tự tìm số điện thoại hoặc kênh liên hệ phù hợp.    │
│ 3. Cư dân trình bày vấn đề với bộ phận tiếp nhận đầu tiên.   │
│ 4. Nếu không đúng thẩm quyền, yêu cầu được chuyển sang       │
│    phòng ban khác; cư dân phải cung cấp lại thông tin.       │
│ 5. Cư dân tiếp tục liên hệ để hỏi tiến độ và kết quả xử lý.  │
│                                                              │
│ Bước nào tốn thời gian/lỗi nhất?                             │
│ Bước 2–4: Xác định đầu mối, phân loại và chuyển tiếp yêu cầu.│
│ Thông tin bị phân tán, thiếu lịch sử trao đổi thống nhất.    │
│                                                              │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                        │
│ AI tiếp nhận yêu cầu qua một đầu mối chung, đọc hiểu nội     │
│ dung, xác định nhóm vấn đề và đề xuất đúng phòng ban         │
│ Vinhomes hoặc Vinpearl phụ trách. Đồng thời lưu lại lịch sử  │
│ trao đổi để cư dân không phải trình bày lại nhiều lần.      │
│                                                              │
│ Đo thành công bằng gì (Metric có số)?                        │
│ 1. Độ chính xác phân loại và điều hướng đạt ≥ 90%            │
│    trên tập kiểm thử 100 yêu cầu.                            │
│ 2. Giảm ít nhất 50% số lần cư dân phải cung cấp lại          │
│    thông tin khi chuyển phòng ban.                           │
│ 3. 100% yêu cầu có mã tiếp nhận và trạng thái theo dõi.      │
│                                                              │
│ Quick Architecture: [ ] No AI [ ] Rule [x] LLM [ ] Agent    │
│                                                              │
│ Operational Boundary: AI chỉ tiếp nhận, phân loại,           │
│ lưu lịch sử và đề xuất phòng ban phụ trách. Không tự ý       │
│ phê duyệt pháp lý, quyết định phí dịch vụ, cam kết quyền lợi │
│ hoặc xử lý các yêu cầu vượt thẩm quyền. Các quyết định       │
│ quan trọng phải do nhân viên có thẩm quyền phê duyệt.        │
└──────────────────────────────────────────────────────────────┘
```

## Card #3 — VinFast: Đối chiếu hóa đơn sạc điện đối tác

```text

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Khối tài chính VinFast phải so khớp hóa   │
│ đơn sạc điện hằng tuần từ hàng nghìn trụ sạc đối tác ngoài  │
│ với số liệu hệ thống — lặp lại, dễ sai sót.                 │
│                                                             │
│ Công ty thành viên: [x] VinFast                             │
│                                                             │
│ Ai đang đau (Actor)?                                        │
│ Nhân viên khối tài chính / quản lý trạm sạc liên kết.       │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Nhận file hóa đơn từ trạm đối tác                      │
│   2. So khớp tay từng dòng với số liệu hệ thống             │
│   3. Bóc tách các sai lệch về tiền/kWh/giờ sạc              │
│   4. Lập bảng đối chiếu gửi trả đối tác                     │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                            │
│ Bước 2–3 (⏱ nhiều giờ/tuần theo đợt đối chiếu, dễ xem nhầm  │
│ số liệu giữa các định dạng file khác nhau).                 │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                       │
│ Bước 2–3: LLM đọc hóa đơn định dạng tự do + so khớp         │
│ trường dữ liệu, tự động flag những dòng nghi ngờ.           │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ 1) Tự động so khớp được ≥ 95% hóa đơn.                      │
│ 2) Thời gian hoàn tất đợt đối chiếu giảm ≥ 70%.             │
│                                                             │
│ Quick Architecture: [x] Rule (+LLM đọc định dạng tự do)      │
│ (Phần số liệu chuẩn dùng rule; LLM chỉ xử lý phần định dạng │
│ tự do — không cần Agent tự trị)                             │
└─────────────────────────────────────────────────────────────┘
```

## Card #5 — Vinmec: Soạn tóm tắt hồ sơ xuất viện

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #5                                       │
│                                                             │
│ Bài toán (1 câu): Bác sĩ Vinmec mất 20–30 phút/bệnh nhân    │
│ để tự tổng hợp và soạn tóm tắt hồ sơ xuất viện.             │
│                                                             │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau (Actor)?                                        │
│ - Bác sĩ (quá tải thời gian, viết cũ rích)                  │
│ - Bệnh nhân (chờ hồ sơ ra viện, khó hiểu thuật ngữ)         │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Bác sĩ xem bệnh án điện tử / xét nghiệm / ghi chú      │
│   2. Tự tổng hợp chẩn đoán & chỉ định                       │
│   3. Tự soạn tóm tắt xuất viện                              │
│   4. Tự soát lỗi & chỉnh văn phong cho phù hợp bệnh nhân    │
│   5. In & ký duyệt, giao cho bệnh nhân                      │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                            │
│ Bước 2–4 (⏱ ước tính 20–30 phút/bệnh nhân).                 │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                       │
│ Bước 2–4: LLM draft tóm tắt từ dữ liệu lâm sàng             │
│ (bác sĩ luôn duyệt 100% trước khi ký).                      │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ 1) Thời gian soạn tóm tắt giảm xuống ≤ 5 phút/bệnh nhân.    │
│ 2) 100% hồ sơ xuất viện có bác sĩ phê duyệt trước khi giao. │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
│ ⚠️ Mảng Y tế nhạy cảm → bắt buộc HITL (bác sĩ duyệt 100%).   │
└─────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Lựa chọn ưu tiên của cá nhân

Nhóm mình nên Deep-Dive: **Card #1 — Vinhomes: Tiếp nhận và xử lý yêu cầu hỗ trợ cư dân/chủ sở hữu BĐS nghỉ dưỡng thuộc hệ sinh thái Vinhomes – Vinpearl.**.

**Lý do chọn và vì sao loại các card khác:**

- **Card #3 (VinFast hóa đơn sạc):**  Đây là bài toán có tính khả thi nhưng ưu tiên thứ hai vì chủ yếu liên quan đến hoạt động back-office, không tác động trực tiếp nhiều đến trải nghiệm khách hàng. Quy trình đối chiếu số liệu có thể giải quyết phần lớn bằng các công cụ xử lý dữ liệu và Rule-based, do đó chưa khai thác được nhiều giá trị nổi bật của LLM.
- **Card #5 (Vinmec):** Bài toán có tiềm năng tiết kiệm thời gian cho bác sĩ nhưng thuộc lĩnh vực y tế nhạy cảm, liên quan trực tiếp đến thông tin và hồ sơ bệnh án. Việc ứng dụng AI đòi hỏi yêu cầu nghiêm ngặt về bảo mật, độ chính xác và sự phê duyệt của bác sĩ, vì vậy chưa thực sự phù hợp để triển khai thử nghiệm nhanh trong phạm vi một buổi Lab.
- **Card #1 (Vinhomes):** Đây là bài toán được ưu tiên lựa chọn vì giải quyết trực tiếp khó khăn của cư dân khi phải liên hệ nhiều đầu mối khác nhau như Ban quản lý, bộ phận phí dịch vụ, pháp lý Vinhomes và dịch vụ nghỉ dưỡng Vinpearl. Việc thiếu một đầu mối hỗ trợ chung khiến cư dân mất thời gian, phải cung cấp lại thông tin nhiều lần và khó theo dõi tiến độ xử lý yêu cầu. AI có thể hỗ trợ tiếp nhận tập trung, đọc hiểu nội dung, phân loại nhu cầu, xác định đúng phòng ban phụ trách và lưu trữ lịch sử trao đổi. Đặc biệt, ranh giới vận hành được xác định rõ: AI chỉ tiếp nhận, phân loại, đề xuất điều hướng và hỗ trợ theo dõi yêu cầu; các quyết định về pháp lý, tài chính, quyền lợi và xử lý chuyên môn phải do nhân viên có thẩm quyền phê duyệt. Giải pháp có khả năng triển khai thử nghiệm trong phạm vi hẹp, có thể đo lường hiệu quả và mở rộng kết nối giữa Vinhomes – Vinpearl trong tương lai.