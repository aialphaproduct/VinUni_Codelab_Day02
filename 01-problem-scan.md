# 01-problem-scan.md — Ý tưởng cá nhân & Nhóm (Vin Smart Future)

> **Học viên:** Khổng Tiến Dương · **Branch cá nhân:**khongtienduong  · **Lab 02: AI Product Scoping**
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
| 1 | **Vinhomes** | Lặp lại | Mỗi ngày BQL nhận hàng trăm phản ánh/khiếu nại cư dân qua App Vinhomes Resident (mất nước, hỏng đèn, ồn ào, thang máy...) và phải **phân loại + điều hướng thủ công từng ticket** đến đúng bộ phận/quy trình xử lý. |
| 2 | **Vinhomes** | AI có thể tốt hơn | CSKH/BQL trả lời cư dân rập khuôn, chậm (vài tiếng đến hơn 1 ngày); chất lượng trả lời không nhất quán giữa các tòa dù cùng hệ thống App. |
| 3 | **VinFast** | Lặp lại | So khớp hóa đơn sạc điện hằng tuần từ hàng nghìn trụ sạc đối tác ngoài với số liệu hệ thống tài chính — khối lượng lặp lại lớn, dễ sai sót do đối chiếu tay. |
| 4 | **Xanh SM** | Pain từ người khác | Tài xế phàn nàn hệ thống gợi ý điểm đón khách không chính xác; phản hồi của tài xế bị điều vận xử lý thủ công từng cuốc qua tổng đài. |
| 5 | **Vinmec** | Tốn thời gian | Bác sĩ soạn tóm tắt hồ sơ xuất viện (Discharge Summary) thủ công ~20–30 phút/bệnh nhân, gây quá tải trong khi hồ sơ là bắt buộc để ra viện. |
| 6 | **Vinpearl** | Pain từ người khác | Phàn nàn khẩn cấp trong review khách sạn ("phòng bẩn", "nhân viên thái độ tệ") bị trôi giữa hàng nghìn review trên Booking/Agoda/Google Maps, đến Manager chậm hoặc không được lọc đúng mức độ. |

*(Danh sách khởi điểm có tham khảo các gợi ý trong `03-inspiration-kit.md`, sau đó tự lọc lại theo lens riêng của từng bài.)*

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn top 3 bài toán từ bảng SCAN để hoàn thiện Quick Problem Cards: **#1 (Vinhomes), #3 (VinFast), #5 (Vinmec)**.

## Card #1 — Vinhomes: Phân loại & điều hướng khiếu nại cư dân 🔥 TOP PICK

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Mỗi ngày ban quản lý (BQL) Vinhomes nhận  │
│ hàng trăm phản ánh cư dân qua App Vinhomes Resident và phải │
│ phân loại + điều hướng thủ công, dẫn đến xử lý chậm và sai  │
│ bộ phận tiếp nhận.                                          │
│                                                             │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau (Actor)?                                        │
│ - Ban quản lý từng tòa (quá tải, phân tay)                  │
│ - CSKH Vinhomes (bám từng ticket, nhắc chồng chéo)          │
│ - Cư dân (chờ lâu, bị chuyển nhầm nơi xử lý)                │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi phản ánh trên App                           │
│   2. BQL đọc và tự phân loại đúng nhóm vấn đề               │
│      (điện nước / thang máy / an ninh / tiện ích...)        │
│   3. Điều hướng đúng bộ phận / nhà thầu kỹ thuật phụ trách  │
│   4. Dedicated nhân viên xử lý + soạn tin trả lời cư dân    │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                            │
│ Bước 2–3 — khâu phân loại và điều hướng (⏱ ước tính         │
│ 10–15 phút/lượt; ticket sai bộ phận phải làm lại toàn bộ).   │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                       │
│ Bước 2–3: LLM phân loại ngữ nghĩa nội dung ticket            │
│ + đề xuất đúng bộ phận xử lý ngay khi cư dân gửi.           │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ 1) Độ chính xác phân loại ≥ 90% trên tập test 100 ticket.   │
│ 2) Thời gian phân loại–điều hướng giảm từ 10–15 phút         │
│    xuống dưới 2 phút/ticket.                                │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
│ (LLM Feature — phân loại & trả lời gợi ý, có rule fallback) │
└─────────────────────────────────────────────────────────────┘
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

Nhóm mình nên Deep-Dive: **Card #1 — Vinhomes: Phân loại & điều hướng khiếu nại cư dân**.

**Lý do chọn và vì sao loại các card khác:**

- **Card #3 (VinFast hóa đơn sạc):** đáng làm nhưng ưu tiên 2 vì là tác vụ back-office hằng tuần, không tác động trực tiếp đến trải nghiệm khách hàng; phần xử lý hóa đơn chuẩn có thể giải bằng parse/rule cổ điển, giá trị LLM chỉ ở phần định dạng tự do → giá trị/list điểm AI thấp hơn.
- **Card #5 (Vinmec):** xử lý tiềm năng cao (tiết kiệm thời gian bác sĩ) nhưng mảng Y tế cực kỳ nhạy cảm — nằm trong lưu ý quan trọng của Inspiration Kit *"Ở các mảng nhạy cảm như Vinmec (Y Tế) hay VinFast (An toàn xe), ranh giới an toàn phải cực kỳ nghiêm ngặt và luôn luôn yêu cầu Human-in-the-loop"* — cần pháp lý phê duyệt rất kỹ, không phù hợp pilot nhanh trong scope 1 buổi lab.
- **Card #1 (Vinhomes):** chạm cả 3 góc — tốn thời gian (BQL phân tay), tỷ lệ sai điều hướng cao, tác động trực tiếp đến trải nghiệm cư dân hàng ngày; và ranh giới AI dễ lí giải rõ ràng (**AI chỉ phân loại + draft tin phản hồi, người duyệt trước khi gửi** — ý tưởng rất giống ranh [DRAFT_ONLY] của worked example) → pilot đơn giản, có số liệu test, và an toàn.
