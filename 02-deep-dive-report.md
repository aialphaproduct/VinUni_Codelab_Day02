# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

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

> **Bài toán được chọn:** Xanh SM (GSM) — Phân tích lý do hủy chuyến từ ghi âm cuộc gọi + ghi chú tài xế để tìm pattern lỗi hệ thống.

---

## 3.1. Current-State Workflow Mapping (25 min)

**Vẽ quy trình hiện tại lên bảng/giấy A3.** Sử dụng các ký hiệu:

- 🔴 **Bottleneck:** Bước gây tắc nghẽn, tốn thời gian, hoặc sai sót nhiều nhất.
- 🔄 **Handoff:** Điểm chuyển giao thông tin giữa người và hệ thống, hoặc giữa các bộ phận.
- Ghi rõ thời gian vận hành trung bình: **Tổng cộng = 15 phút/chuyến**.

```text
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Bước 1       │   │ Bước 2       │   │ Bước 3       │   │ Bước 4       │   │ Bước 5       │
│ Hệ thống thu │   │ QA nghe lại  │   │ Phân loại    │   │ Tổng hợp     │   │ Rà pattern   │
│ ghi âm + log │──→│ từng cuộc gọi│──→│ lý do hủy    │──→│ vào Excel/   │──→│ lỗi hệ thống │
│ chuyến hủy   │   │ + ghi chú tay│   │ vào danh mục │   │ báo cáo      │   │ thủ công     │
│              │   │              │   │              │   │ định kỳ      │   │              │
│ Ai: Hệ thống │   │ Ai: Chuyên   │   │ Ai: Chuyên   │   │ Ai: Chuyên   │   │ Ai: Trưởng   │
│ (tự động)    │   │ viên QA      │   │ viên QA      │   │ viên QA      │   │ nhóm QA      │
│ ⏱ 1 phút     │   │ ⏱ 8 phút 🔴  │   │ ⏱ 4 phút 🔴  │   │ ⏱ 2 phút     │   │ ⏱ 2 phút     │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
                    🔄 Handoff         🔄 Handoff         🔄 Handoff         🔄 Handoff
                    (log → con người)  (ghi chú → danh mục)(danh mục → báo cáo)(báo cáo → lãnh đạo)
```

🔴 = Bottleneck (Bước 2 & 3, tổng 12 phút)
⏱ Tổng thời gian xử lý thủ công: **15 phút/chuyến hủy**.

---

## 3.2. Problem Statement (6-field) & Metrics (15 min)

| Field                       | Nội dung chi tiết                                                                                                                                                                                                                                                                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Actor / Operator**     | Chuyên viên QA thuộc **nhóm Vận hành & Chất lượng dịch vụ Xanh SM (GSM)** thực hiện hằng ngày; Trưởng nhóm QA tổng hợp và báo cáo lên lãnh đạo.                                                                                                                                                                                             |
| **2. Current Workflow**     | Khi có chuyến hủy, hệ thống tự thu thập ghi âm cuộc gọi + ghi chú tài xế. Chuyên viên QA **nghe lại từng cuộc gọi**, ghi chú thủ công, **phân loại lý do hủy** vào danh mục (khách đổi ý / điểm đón sai / lỗi app…), rồi tổng hợp vào Excel/báo cáo định kỳ và rà pattern lỗi hệ thống. 5 bước, hoàn toàn thủ công, mất 15 phút/chuyến. |
| **3. Bottleneck**           | **Bước 2 & 3 (12 phút):** nghe lại toàn bộ ghi âm và phân loại lý do hủy thủ công. Đây là tác vụ **xử lý ngôn ngữ tự nhiên** (nghe hiểu tiếng Việt, suy luận ngữ cảnh) — khó tự động hoá bằng rule đơn thuần.                                                                                                                              |
| **4. Business Impact**      | Ước tính ~200 chuyến hủy/ngày → lãng phí **~50 giờ/ngày (~6 FTE)** cho việc phân tích thủ công. Pattern lỗi hệ thống (ví dụ: điểm đón bị lệch GPS ở một khu vực) chỉ lộ ra khi báo cáo cuối tuần/tháng, nên lỗi **lan rộng nhiều ngày** trước khi được sửa → tăng tỉ lệ hủy, giảm doanh thu và trải nghiệm khách hàng.                     |
| **5. Success Metric**       | 1. Giảm thời gian phân tích từ **15 phút → dưới 2 phút/chuyến** (Efficiency).<br>2. **Độ chính xác phân loại lý do ≥ 90%** so với nhãn QA (Quality).<br>3. **Phát hiện pattern lỗi hệ thống sớm hơn 2 tuần** so với quy trình báo cáo hiện tại (Time-to-insight).                                                                          |
| **6. Operational Boundary** | AI **được phép:** transcribe ghi âm, phân loại lý do hủy, gợi ý pattern lỗi hệ thống dạng nháp. **TUYỆT ĐỐI CẤM:** tự kết luận/quy kết lỗi cá nhân tài xế (chỉ phân tích pattern hệ thống, không dùng để xử lý kỷ luật); gửi báo cáo lên lãnh đạo khi chưa có chuyên viên QA duyệt (bắt buộc HITL); suy diễn nguyên nhân ngoài dữ liệu có trong transcript. |

---

## 3.3. Future-State Flow & AI Fit (25 min)

- **Xác định mức AI Fit (AI-Fit Matrix):** Giải pháp thuộc nhóm **[x] LLM Feature** — transcribe + phân loại + tổng hợp ngữ nghĩa. Không cần **Agentic Loop** vì quy trình phân tích offline có cấu trúc cố định, không đòi hỏi vòng lặp tự trị ra quyết định. Bước "tìm pattern" được thực hiện bằng **aggregation/clustering (rule/statistics)** trên nhãn do LLM sinh ra.
- **Vẽ Future-State Flow:** Đánh dấu rõ:
  - 🔵 **AI Step:** Tác vụ LLM xử lý.
  - 🟢 **Human Step (HITL):** Bước con người phê duyệt/review (Human-in-the-loop).
  - ↩️ **Fallback:** Kế hoạch dự phòng khi LLM trả về kết quả lỗi hoặc không tự tin.

```text
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Bước 1       │   │ Bước 2       │   │ Bước 3       │   │ Bước 4       │   │ Bước 5       │
│ Hệ thống thu │   │ 🔵 AI Step   │   │ 🔵 AI Step   │   │ 🔵 AI Step   │   │ 🟢 HITL      │
│ ghi âm + log │──→│ Speech-to-   │──→│ LLM phân loại│──→│ Gom pattern  │──→│ QA xác nhận  │
│ chuyến hủy   │   │ text transcript│ │ lý do + trích│   │ lỗi hệ thống │   │ nhãn + duyệt │
│ (tự động)    │   │ ghi âm       │   │ xuất ngữ cảnh│   │ (thống kê)   │   │ báo cáo      │
│ ⏱ 0 phút     │   │ ⏱ vài giây   │   │ ⏱ vài giây   │   │ ⏱ vài giây   │   │ ⏱ 1 phút     │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
                                                    │
                                                    ▼
                                    ↩️ Fallback: transcript độ tin cậy thấp
                                    (nhiễu, không nghe rõ) hoặc LLM không
                                    tự tin → đánh dấu "chưa xác định" và
                                    chuyển lại cho QA nghe thủ công như cũ.
```

---

# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

### AI Readiness Checklist:

1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?
   → **Có, một phần.** Xanh SM đã lưu ghi âm cuộc gọi + ghi chú tài xế + log chuyến hủy, và App có mã lý do hủy do khách/tài xế chọn (có thể dùng làm nhãn yếu ban đầu). Cần dọn dữ liệu nhiễu (tiếng ồn, tiếng địa phương) và xây tập nhãn chuẩn do QA gán.
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)?
   → **Có.** Đây là phân tích offline (back-office), kết quả không ảnh hưởng real-time hay an toàn. Mọi nhãn/báo cáo đều qua QA duyệt trước khi dùng; trường hợp transcript không rõ sẽ fallback về nghe thủ công.
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?
   → **Khá sẵn sàng.** Nhóm QA đang quá tải (15 phút/chuyến) và muốn giảm tải phần nghe lại. Điểm cần lưu ý: lãnh đạo cần cam kết AI **chỉ phân tích pattern hệ thống, không dùng để quy kết lỗi cá nhân** để tránh phản kháng từ tài xế.

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:

- [x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
- [ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
- [ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**

> **GO với scope hẹp** vì bài toán có đủ 3 điều kiện:
> 1. **Rủi ro thấp, kiểm soát được:** phân tích offline, không đụng đến an toàn hay quyết định real-time, và luôn có HITL + Fallback (transcript không rõ → nghe thủ công).
> 2. **LLM fit rõ ràng:** lõi bài toán là "nghe hiểu + phân loại + tóm tắt ngôn ngữ tự nhiên" — đúng thế mạnh của LLM, không thể giải bằng rule đơn thuần.
> 3. **Metric đo được:** thời gian 15 phút → dưới 2 phút/chuyến, độ chính xác ≥ 90%, phát hiện pattern sớm hơn 2 tuần.
>
> **Scope prototype:** pilot trên **1 thành phố, 1 tuần dữ liệu chuyến hủy**, QA gán nhãn chuẩn cho ~200 mẫu để đo baseline, trước khi mở rộng toàn quốc.
>
> **Rủi ro cần theo dõi:** chất lượng Speech-to-text cho tiếng Việt (nhiễu, tiếng địa phương) có thể kéo độ chính xác xuống dưới ngưỡng 90%; nếu sau pilot không đạt, quay lại trạng thái **NOT YET** để tích luỹ dữ liệu và cải thiện mô hình transcribe trước khi scale.
