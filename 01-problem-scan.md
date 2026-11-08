# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

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

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:

1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **🤖 AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> _"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."_

### 📝 List bài toán của tôi:

| #   | Subsidiary (VinFast/Xanh SM...) | Lens                                  | Mô tả ngắn bài toán                                                                                                                                                                                |
| --- | ------------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | VinFast                         | Lặp lại (Repetitive)                  | Đối chiếu hóa đơn sạc điện hằng tuần từ hàng nghìn trụ sạc đối tác với số liệu nội bộ (hiện làm thủ công trên Excel).                                                                              |
| 2   | Vinhomes                        | AI-upgrade                            | Phân loại & điều hướng khiếu nại cư dân trên App Vinhomes Resident (mất nước, hỏng thang máy...) đến đúng ban quản lý.                                                                             |
| 3   | Vinmec                          | Tốn thời gian (Time-consuming)        | Soạn tóm tắt hồ sơ xuất viện từ bệnh án điện tử + xét nghiệm + ghi chú bác sĩ (20-30 phút/ca).                                                                                                     |
| 4   | Xanh SM (GSM)                   | Tốn thời gian (Time-consuming)        | Phân tích lý do hủy chuyến từ ghi âm cuộc gọi + ghi chú tài xế để tìm pattern lỗi hệ thống.                                                                                                        |
| 5   | Vinhomes / Vinpearl             | Pain từ người khác (Stakeholder Pain) | Hợp nhất đầu mối cư dân ↔ Vingroup: cư dân/chủ sở hữu BĐS nghỉ dưỡng phải gọi riêng lẻ nhiều bộ phận (BQL phí dịch vụ, pháp lý, dịch vụ nghỉ dưỡng) và lặp lại thông tin mỗi lần chuyển phòng ban. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #___                                     │
│                                                             │
│ Bài toán (1 câu): ________________________________________  │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? ______________________________________ │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. ___ ──> 2. ___ ──> 3. ___ ──> 4. ___                   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? ___ (⏱ ___ phút/lượt)      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? _____________________ │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? ______________________ │
│   VD: "Giảm thời gian soạn phản hồi từ 10 min ──> under 2 min"│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

## 3 Quick Problem Cards của tôi (Top 3 tiềm năng nhất)

Chọn top 3 từ danh sách SCAN: **#3 (Vinmec tóm tắt hồ sơ xuất viện), #2 (Vinhomes phân loại khiếu nại), #4 (Xanh SM phân tích lý do hủy chuyến).**

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Bác sĩ tốn 20-30 phút để soạn tóm tắt hồ sơ xuất   │
│ viện từ bệnh án điện tử, kết quả xét nghiệm và ghi chú bác sĩ.│
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ điều trị (quá tải), bệnh nhân    │
│ chờ đợi lâu, nhân viên hành chính y tế.                      │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Bác sĩ đọc bệnh án điện tử + kết quả xét nghiệm         │
│   → 2. Đọc ghi chú diễn biến điều trị của các ca trực         │
│   → 3. Tổng hợp thông tin, soạn tóm tắt xuất viện            │
│   → 4. Rà soát thuốc, liều lượng và lời dặn tái khám         │
│   → 5. Ký duyệt và bàn giao cho bệnh nhân                    │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 1-3 (⏱ 20-30 phút/ca) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1-3               │
│ (Đọc + trích xuất dữ liệu → soạn bản nháp tóm tắt xuất viện) │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian soạn từ 25 phút ──> dưới 5 phút/ca (bản nháp  │
│ dùng được ≥ 80%); tỉ lệ sai sót thuốc/liều lượng < 0.5%.     │
│                                                             │
│ Quick Architecture: [x] LLM  (HITL: bác sĩ duyệt trước khi ký)│
└─────────────────────────────────────────────────────────────┘
```

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Phân loại & điều hướng khiếu nại cư dân trên App   │
│ Vinhomes Resident (mất nước, hỏng thang máy...) đến đúng BQL.│
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau (Actor)? Cư dân (chờ lâu), nhân viên CSKH,       │
│ Ban quản lý (BQL) tòa nhà.                                  │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Cư dân gửi khiếu nại qua App Vinhomes Resident          │
│   → 2. CSKH đọc & đoán loại sự cố (nước/thang máy/an ninh)  │
│   → 3. Tìm đúng BQL/phòng ban phụ trách theo từng tòa        │
│   → 4. Chuyển ticket + ghi chú thủ công                      │
│   → 5. Theo dõi trạng thái xử lý và phản hồi lại cư dân      │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ 10-15 phút/lượt)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4               │
│ (Tự phân loại sự cố → route đúng BQL → soạn phản hồi draft)  │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian route từ 15 phút ──> dưới 30 giây; tỉ lệ      │
│ route đúng BQL đạt ≥ 95%; giảm khiếu nại lặp lại 30%.        │
│                                                             │
│ Quick Architecture: [x] LLM  (Rule router → LLM phân loại +   │
│ draft phản hồi)                                             │
└─────────────────────────────────────────────────────────────┘
```

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Phân tích lý do hủy chuyến từ ghi âm cuộc gọi và   │
│ ghi chú tài xế để tìm pattern lỗi hệ thống.                  │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau (Actor)? Nhóm vận hành & chất lượng dịch vụ       │
│ Xanh SM, tài xế (ảnh hưởng thu nhập), khách hàng hủy chuyến. │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Thu thập ghi âm cuộc gọi + ghi chú tài xế của chuyến hủy│
│   → 2. Nhân viên nghe lại từng cuộc gọi, ghi chú thủ công    │
│   → 3. Phân loại lý do hủy (khách đổi ý/điểm đón sai/lỗi app)│
│   → 4. Tổng hợp vào bảng Excel/báo cáo định kỳ               │
│   → 5. Rà pattern thủ công để tìm lỗi hệ thống lặp lại        │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ 15-20 phút/chuyến)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-5               │
│ (Tự transcript ghi âm → phân loại lý do → gom pattern lỗi)   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian phân tích từ 15 phút ──> dưới 2 phút/chuyến;   │
│ độ chính xác phân loại lý do ≥ 90%; phát hiện pattern lỗi     │
│ hệ thống sớm hơn 2 tuần.                                     │
│                                                             │
│ Quick Architecture: [x] LLM  (transcribe + classify, báo cáo  │
│ có HITL kiểm tra trước khi gửi lãnh đạo)                     │
└─────────────────────────────────────────────────────────────┘
```
