# Lab 02 — Worksheet: AI Product Scoping (Vin Smart Future)

---

## 🏛️ 1. Bối cảnh thực tế: Vin Smart Future (Vingroup)

**Vingroup** — Tập đoàn tư nhân lớn nhất Việt Nam — vừa sáp nhập toàn bộ các phòng ban công nghệ thuộc các công ty thành viên thành một đơn vị công nghệ thống nhất mang tên **Vin Smart Future**.

Nhiệm vụ của **Vin Smart Future** là xây dựng các giải pháp AI, số hóa, và tự động hóa cốt lõi để nâng cao hiệu suất vận hành và trải nghiệm khách hàng xuyên suốt các công ty thành viên:

- 🚗 **VinFast:** Hệ thống xe điện thông minh (EV), trợ lý AI ảo trong xe, dự đoán bảo trì pin, và quản lý chuỗi cung ứng sản xuất.
- 🚕 **Xanh SM (GSM):** Vận hành đội xe taxi/xe máy điện thông minh, điều vận thông minh (Smart Dispatching), tối ưu hóa lộ trình di chuyển.
- 🏢 **Vinhomes:** Quản lý đô thị thông minh (Smart Cities), trợ lý cư dân thông minh, tối ưu hóa mức tiêu thụ năng lượng.
- 🏥 **Vinmec:** Y tế thông minh, chẩn đoán hình ảnh bằng AI, tối ưu hóa quản lý hồ sơ bệnh án.
- 🎢 **Vinpearl / VinWonders:** Trải nghiệm du lịch số hóa, quản lý phòng và luồng khách thông minh tại các khu vui chơi.

Trong buổi Lab hôm nay, nhóm của bạn sẽ đóng vai trò là **AI Product Engineer** tại **Vin Smart Future**, tiến hành tìm kiếm, scoping, phân tích độ khả thi, thiết lập ranh giới vận hành, và xây dựng một **bản mẫu kỹ thuật (prompt prototype)** cho một bài toán cụ thể thuộc một trong những mảng kinh doanh trên.

---

## 📊 2. Cơ cấu tính điểm bài lab

### 👥 Điểm nhóm (60 điểm)

| Gate                         | Điểm | Deliverable       | Tiêu chí chấm                                                                |
| ---------------------------- | ---: | ----------------- | ---------------------------------------------------------------------------- |
| **G1. Workflow Mapping**     |   20 | Problem Deep-Dive | Vẽ chi tiết quy trình hiện tại: các bước, handoff, thời gian, bottleneck     |
| **G2. Problem Statement**    |   20 | Problem Deep-Dive | Problem Statement 6-field bám sát thực tế, metric có số và ranh giới rõ ràng |
| **G3. AI Fit & Future Flow** |   10 | Problem Deep-Dive | So sánh Rule vs LLM vs Agent, future flow có bước AI, ranh giới và Fallback  |
| **G4. Decision Quality**     |   10 | Problem Deep-Dive | Quyết định Go/Not Yet/No-Go trung thực và có chứng cứ rõ ràng                |

### 👤 Điểm cá nhân (40 điểm)

| Gate                        | Điểm | Deliverable  | Tiêu chí chấm                                                                     |
| --------------------------- | ---: | ------------ | --------------------------------------------------------------------------------- |
| **I1. Scan & Cards**        |   15 | Quick Cards  | Liệt kê 5 problems sử dụng 3 lenses, hoàn thiện 3 quick cards chất lượng          |
| **I2. Prototyping**         |   10 | 02-lab/      | Chạy thử nghiệm programmatic prompt prototype thành công                          |
| **I3. AI Log & Reflection** |   15 | 03-ai-log.md | Phản ánh trung thực về việc dùng AI làm thought-partner (giúp gì, sai gì, sửa gì) |

---

# 🚀 Phase 0 — worked Example: Xanh SM Intelligent Dispatcher (15 min)

_Giảng viên walk-through ví dụ thực tế từ Vin Smart Future để bạn hiểu rõ cách scoping một bài toán AI._
Đọc chi tiết worked example tại file [02-deliverable-example.md](02-deliverable-example.md).

---

# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

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

| #   | Subsidiary (VinFast/Xanh SM...) | Lens             | Mô tả ngắn bài toán                                                                                                   |
| --- | ------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1   | Vinmec                          | Repetitive       | Nhập liệu và chuẩn hóa hồ sơ bệnh án từ nhiều loại giấy tờ, kết quả xét nghiệm và biểu mẫu khác nhau.                 |
| 2   | Vinmec                          | Time-consuming   | Kiểm tra, đối chiếu hồ sơ bảo hiểm y tế và xử lý các yêu cầu bổ sung giấy tờ trước khi thanh toán.                    |
| 3   | Vinmec                          | AI-upgrade       | Tối ưu quy trình đặt lịch khám, nhắc lịch và hỗ trợ sắp xếp lại lịch khi bệnh nhân hủy hoặc không đến khám.           |
| 4   | Vinmec                          | Repetitive       | Đối soát viện phí, mã dịch vụ và hóa đơn giữa hồ sơ điều trị với hệ thống thanh toán.                                 |
| 5   | Vinmec                          | Stakeholder Pain | Bác sĩ mất nhiều thời gian soạn thảo, nhập liệu và hoàn thiện báo cáo khám chữa bệnh thay vì tập trung vào bệnh nhân. |

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
│ Bước nào tốn thời gian/lỗi nhất? ___  (⏱ __ phút/lượt)      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? _____________________ │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? _____________________ │
│ VD: "Giảm thời gian soạn phản hồi từ 10 min ──> under 2 min"│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **🤖 AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> _"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."_

Trong 5 bài toán mình vừa nêu trên thì mình sẽ chọn 3 bài toán mà cảm thấy là khó khăn và khó giải quyết nhất. Đó là 3 bài:

- Problem #2: Kiểm tra và đối chiếu hồ sơ bảo hiểm.
- Problem #4: Đối soát viện phí, mã dịch vụ và hóa đơn.
- Problem #5: Soạn thảo và hoàn thiện hồ sơ khám chữa bệnh.

1. Problem #2: Kiểm tra và đối chiếu hồ sơ bảo hiểm.
<!-- prettier-ignore-start -->

```
┌──────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                │
│                                                                      │
│ Bài toán (1 câu):                                                    │
│ Tự động kiểm tra quyền lợi bảo hiểm và phát hiện hồ sơ thiếu giấy tờ │
│ trước khi gửi yêu cầu phê duyệt thanh toán.                          │
│                                                                      │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes           │
│                     [x] Vinmec   [ ] Khác: __________                │
│                                                                      │
│ Ai đang đau (Actor)?                                                 │
│ Nhân viên bảo hiểm, nhân viên tiếp nhận và thanh toán viện phí.      │
│                                                                      │
│ Workflow thủ công hiện tại (3-5 bước):                               │
│ 1. Tiếp nhận yêu cầu --> 2. Kiểm tra quyền lợi bảo hiểm              │
│ --> 3. Đối chiếu dịch vụ --> 4. Kiểm tra giấy tờ --> 5. Gửi duyệt    │
│                                                                      │
│ Bước nào tốn thời gian/lỗi nhất?                                     │
│ Kiểm tra và xử lý prior authorization.                               │
│ (Benchmark: 24 phút/giao dịch thủ công - CAQH 2024)                  │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                │
│ OCR trích xuất, LLM đọc điều khoản và cảnh báo hồ sơ thiếu.          │
│                                                                      │
│ Đo thành công bằng gì (Metric có số)?                                │
│ Benchmark CAQH: 24 phút thủ công --> 10 phút điện tử.                │
│ Mục tiêu khảo sát: đo thời gian xử lý và tỷ lệ hồ sơ bị từ chối.     │
│                                                                      │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent          │
└──────────────────────────────────────────────────────────────────────┘

```

Nguồn trích dẫn: CAQH 2024 Index và khảo sát AMA 2024.

- CAQH: kiểm tra quyền lợi bảo hiểm mất trung bình 16 phút khi làm thủ công, so với 4 phút khi xử lý điện tử.
- CAQH: prior authorization mất 24 phút thủ công, so với 10 phút khi xử lý điện tử.
- AMA: bác sĩ và nhân viên dành trung bình 13 giờ mỗi tuần cho prior authorization; trung bình 39 yêu cầu mỗi bác sĩ mỗi tuần.
<!-- prettier-ignore-end -->

2. Problem #4: Đối soát viện phí, mã dịch vụ và hóa đơn.

<!-- prettier-ignore-start -->
```
┌──────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                │
│                                                                      │
│ Bài toán (1 câu):                                                    │
│ Tự động phát hiện sai lệch giữa chỉ định điều trị, dịch vụ thực tế,  │
│ mã dịch vụ và hóa đơn viện phí.                                      │
│                                                                      │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes           │
│                     [x] Vinmec   [ ] Khác: __________                │
│                                                                      │
│ Ai đang đau (Actor)?                                                 │
│ Nhân viên kế toán viện phí, bộ phận bảo hiểm và tài chính.           │
│                                                                      │
│ Workflow thủ công hiện tại (3-5 bước):                               │
│ 1. Thu thập dịch vụ --> 2. Đối chiếu chỉ định bác sĩ                 │
│ --> 3. Kiểm tra mã và giá --> 4. Đối chiếu hóa đơn                   │
│ --> 5. Phát hiện và xử lý sai lệch.                                  │
│                                                                      │
│ Bước nào tốn thời gian/lỗi nhất?                                     │
│ Đối chiếu dữ liệu và xử lý sai lệch giữa các hệ thống.               │
│ (Benchmark tham khảo: 12 phút/claim submission thủ công - CAQH 2024) │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                │
│ Đối chiếu hóa đơn, phát hiện mã dịch vụ và đơn giá bất thường.       │
│                                                                      │
│ Đo thành công bằng gì (Metric có số)?                                │
│ Benchmark tham khảo: Initial claim denial rate 11,6% (2025).         │
│ Theo dõi tỷ lệ từ chối, tỷ lệ đối soát chính xác và thời gian xử lý. │
│                                                                      │
│ Quick Architecture: [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent          │
└──────────────────────────────────────────────────────────────────────┘
```
Nguồn trích dẫn: CAQH 2024 Index và Kodiak Solutions 2025 Revenue Cycle Benchmark.

- CAQH: gửi yêu cầu thanh toán (claim submission) mất 12 phút thủ công, so với 5 phút khi xử lý điện tử.
- CAQH: tra cứu trạng thái yêu cầu thanh toán mất 25 phút thủ công, so với 7 phút khi xử lý điện tử.
- Kodiak Solutions: tỷ lệ initial claim denial trung bình của các bệnh viện trong bộ dữ liệu năm 2025 là 11,6%, tăng từ 11,4% năm 2024. Dữ liệu tổng hợp từ 2.300 bệnh viện.

<!-- prettier-ignore-end -->

3. Problem #5: Soạn thảo và hoàn thiện hồ sơ khám chữa bệnh.
<!-- prettier-ignore-start -->

```
┌──────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                │
│                                                                      │
│ Bài toán (1 câu):                                                    │
│ Hỗ trợ bác sĩ chuyển nội dung trao đổi và thông tin khám bệnh thành  │
│ bản ghi chú bệnh án có cấu trúc nhằm giảm thời gian nhập liệu.       │
│                                                                      │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes           │
│                     [x] Vinmec   [ ] Khác: __________                │
│                                                                      │
│ Ai đang đau (Actor)?                                                 │
│ Bác sĩ khám chữa bệnh, điều dưỡng và nhân viên quản lý hồ sơ.        │
│                                                                      │
│ Workflow thủ công hiện tại (3-5 bước):                               │
│ 1. Tiếp nhận bệnh nhân --> 2. Ghi nhận triệu chứng và tiền sử        │
│ --> 3. Nhập dữ liệu --> 4. Soạn ghi chú --> 5. Kiểm tra hồ sơ        │
│                                                                      │
│ Bước nào tốn thời gian/lỗi nhất?                                     │
│ Nhập liệu và tổng hợp thông tin vào hồ sơ bệnh án.                   │
│ (Benchmark: 10,3 phút/lượt khám - nghiên cứu JAMA 2025)              │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                │
│ Chuyển giọng nói thành văn bản, tóm tắt và điền mẫu bệnh án.         │
│                                                                      │
│ Đo thành công bằng gì (Metric có số)?                                │
│ Benchmark nghiên cứu: 10,3 --> 8,2 phút/lượt khám (-20,4%).          │
│ Theo dõi độ chính xác nội dung và tỷ lệ ghi chú phải chỉnh sửa.      │
│                                                                      │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent          │
└──────────────────────────────────────────────────────────────────────┘
```

Nguồn trích dẫn: nghiên cứu trên JAMA Network Open năm 2025.

Nghiên cứu trên 46 nhân viên y tế thuộc 17 chuyên khoa cho thấy sau khi sử dụng công cụ AI ambient scribe:

- Thời gian ghi chú mỗi lượt khám giảm từ 10,3 xuống 8,2 phút.
- Giảm 20,4% thời gian ghi chú.
- Thời gian làm hồ sơ ngoài giờ giảm từ 50,6 xuống 35,4 phút/ngày, tương đương giảm 30%.

## <!-- prettier-ignore-end -->

# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

## 3.1. Current-State Workflow Mapping (25 min)

**Vẽ quy trình hiện tại lên bảng/giấy A3.** Sử dụng các ký hiệu:

- 🔴 **Bottleneck:** Bước gây tắc nghẽn, tốn thời gian, hoặc sai sót nhiều nhất.
- 🔄 **Handoff:** Điểm chuyển giao thông tin giữa người và hệ thống, hoặc giữa các bộ phận.
- Ghi rõ thời gian vận hành trung bình: **Tổng cộng = \_\_\_\_ phút/lượt**.

## 3.2. Problem Statement (6-field) & Metrics (15 min)

Điền đầy đủ 6 trường thông tin của bài toán:

| Field                       | Nội dung chi tiết                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------- |
| **1. Actor / Operator**     | Ai đang thực hiện tác vụ hằng ngày?                                                    |
| **2. Current Workflow**     | Mô tả tóm tắt quy trình thủ công hiện tại và công cụ sử dụng.                          |
| **3. Bottleneck**           | Bước nào chậm, lỗi, hoặc cần xử lý ngôn ngữ tự động nhiều nhất?                        |
| **4. Business Impact**      | Tổn thất thực tế đo bằng thời gian, chi phí, hoặc SLA của Vingroup.                    |
| **5. Success Metric**       | AI giải quyết được thì đạt ngưỡng số mấy? (Ví dụ: _"85% vé được phân loại dưới 10s"_). |
| **6. Operational Boundary** | AI được phép làm gì, TUYỆT ĐỐI không được làm gì, điểm nào cần duyệt?                  |

## 3.3. Future-State Flow & AI Fit (25 min)

- **Xác định mức AI Fit (AI-Fit Matrix):** Giải pháp thuộc nhóm nào? [ ] Rule / State-Machine [ ] LLM Feature [ ] Agentic Loop.
- **Vẽ Future-State Flow:** Đánh dấu rõ:
  - 🔵 **AI Step:** Tác vụ LLM xử lý.
  - 🟢 **Human Step (HITL):** Bước con người phê duyệt/review (Human-in-the-loop).
  - ↩️ **Fallback:** Kế hoạch dự phòng khi LLM trả về kết quả lỗi hoặc không tự tin.

---

# 💻 Phase 4 — TECHNICAL PROMPT PROTOTYPE (Nhóm, 30 min)

Để đảm bảo kỹ sư của Vin Smart Future luôn giữ vững năng lực lập trình, nhóm của bạn sẽ tiến hành **lập trình bản mẫu prompt** trực tiếp trên **Gemini 2.5 Flash** bằng Python để stress-test hệ thống.

### Hướng dẫn thực hiện:

1. Mở file [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py) bằng VS Code/Cursor.
2. Hoàn thiện các nội dung sau:
   - **System Prompt:** Viết chỉ thị cực kỳ nghiêm ngặt quy định vai trò, nhiệm vụ, định dạng output và **Operational Boundary (Ranh giới cấm)** của mô hình.
   - **Structured Output:** Định nghĩa định dạng JSON output rõ ràng.
   - **Adversarial Test Cases:** Viết ít nhất 3 prompts "tấn công" (Adversarial inputs) cố tình dụ AI vượt ranh giới hoặc đưa ra câu trả lời không được phép để kiểm tra xem ranh giới của bạn có thực sự vững chắc.
3. Chạy file python:
   ```bash
   python3 prompt_prototype.py
   ```
4. Kiểm tra xem các ranh giới an toàn có bị LLM phá vỡ hay không và ghi lại kết quả vào worksheet.

---

# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

### AI Readiness Checklist:

1. [ ] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?
2. [ ] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)?
3. [ ] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:

[ ] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**

> _Viết lý giải chi tiết tại đây_

---

# 📝 Phase 6 — REFLECTION (Cá nhân)

_Ghi nhận phản ánh của cá nhân bạn về việc phối hợp với AI trong buổi học hôm nay vào file `03-ai-log.md`._
