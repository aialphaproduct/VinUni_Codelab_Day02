# AI Log & Reflection — Nhật ký tương tác cùng AI (Lab 02)

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
> **Môn học / Lab:** Lab 02 — AI Product Scoping (Vin Smart Future)  
> **Công cụ & Mô hình AI sử dụng:** Gemini (Thought-partner phân tích nghiệp vụ & phản biện kiến trúc) + Google Gemini 3.5 Flash API (`gemini-3.5-flash` trong kiểm thử `prompt_prototype.py`)

---

## 1. AI đã giúp ích gì trong vai trò Thought-Partner?

Trong suốt 5 pha của buổi Lab, thay vì yêu cầu AI "viết hộ trọn gói từ đầu", em sử dụng AI như một đối tác tư duy (_thought-partner_) và người phản biện (_devil's advocate_) ở 4 khâu then chốt:

1. **Mở rộng góc nhìn vận hành theo 4 Lenses (Phase 1 — SCAN):**
   - Khi khảo sát mảng y tế **Vinmec**, em dễ bị thiên lệch về các bài toán chẩn đoán hình ảnh lâm sàng vốn rất nặng về cấp phép y tế. Nhờ yêu cầu AI rà soát chuỗi vận hành hành chính – tài chính bệnh viện (_Revenue Cycle Management & Clinical Operations_) qua 4 lăng kính (_Repetitive, Time-consuming, AI-upgrade, Stakeholder Pain_), em nhanh chóng xác định được 5 điểm nghẽn thiết thực hơn nhiều: chuẩn hóa hồ sơ đầu vào, bảo lãnh viện phí (_Prior Authorization_), điều phối lịch hẹn, đối soát viện phí – hóa đơn và ghi chú bệnh án lâm sàng (_Ambient Scribe_).
2. **Đóng vai CFO & Trưởng phòng Vận hành để Stress-Test thẻ bài toán (Phase 2 — QUICK-ASSESS):**
   - Khi đưa cả 3 Quick Problem Cards cho AI phản biện dưới góc nhìn khắt khe của CFO, AI giúp em nhìn ra một quyết định kỹ thuật cực kỳ quan trọng: **Card #2 (Đối soát viện phí, mã dịch vụ và hóa đơn)** không nên dùng LLM! Vì dữ liệu mã dịch vụ trên HIS và hóa đơn trên ERP đều là dữ liệu bảng có cấu trúc, một bộ **Rule-based / SQL Reconciliation** giải quyết chính xác 100% với chi phí gần như bằng 0. Nhờ đó em định vị đúng kiến trúc `[x] Rule` cho Card #2 và dồn nguồn lực LLM cho **Card #1 (Kiểm tra quyền lợi & Hồ sơ Bảo lãnh viện phí)**.
3. **Tra cứu và đối chiếu nguồn số liệu Benchmark ngành y tế uy tín:**
   - AI gợi ý các báo cáo chuẩn quốc tế của ngành quản trị chu trình doanh thu bệnh viện như **CAQH 2024 Index**, **Khảo sát AMA 2024**, **Kodiak Solutions 2025 Revenue Cycle Benchmark** và nghiên cứu lâm sàng trên **JAMA Network Open (2025)**, giúp em thay thế các con số ước đoán cảm tính bằng số liệu định lượng có nguồn trích dẫn rõ ràng.
4. **Thiết kế kịch bản tấn công Prompt Injection (Phase 4 — Prototyping):**
   - AI hỗ trợ em xây dựng kịch bản tấn công kết hợp (_leo thang đặc quyền giả danh Giám đốc Điều vận + ép bỏ nhãn `[DRAFT_ONLY]` + ép vi phạm ngưỡng pin tới hạn `< 5%`_) và chuyển đổi mã nguồn sang SDK `google-genai` mới với model `gemini-3.5-flash`.

---

## 2. Những chỗ AI trả lời sai, Hallucination hoặc đề xuất thiếu thực tế

Quá trình làm việc cùng AI bộc lộ 3 lỗi điển hình mà nếu kỹ sư sản phẩm không kiểm chứng lại sẽ làm hỏng ngay bản đề xuất:

### ❌ Lỗi 1: Bịa đặt số liệu nội bộ (Data Hallucination) & áp máy móc chi phí Mỹ vào Việt Nam

- **Hiện tượng:** Ở lần brainstorm đầu tiên trong Phase 1–2, khi em hỏi về tổn thất vận hành tại Vinmec, AI tự tin đưa ra các con số nghe rất "thật" như _"Vinmec xử lý chính xác X nghìn ca bảo lãnh/ngày với tỷ lệ từ chối 14,2%"_ dù đây là số liệu nội bộ chưa từng công bố. Đồng thời, AI lấy mức lương nhân viên hành chính y tế tại Mỹ (~25–30 USD/giờ từ báo cáo CAQH) nhân thẳng ra tiền tiết kiệm hàng triệu USD cho một bệnh viện tại Việt Nam.
- **Tác hại nếu tin ngay:** Làm mất hoàn toàn tính trung thực của báo cáo trước Ban Giám đốc Vin Smart Future (vi phạm tiêu chí _Decision Quality_).

### ❌ Lỗi 2: Bệnh "sùng bái Multi-Agent" (Architecture Over-Engineering)

- **Hiện tượng:** Khi thiết kế quy trình tương lai (Phase 3.3) cho bài toán Bảo lãnh Viện phí Vinmec, AI ban đầu đề xuất một kiến trúc **Autonomous Multi-Agent** rất hào nhoáng: _Agent 1 đọc bệnh án -> Agent 2 tự động chat yêu cầu bác sĩ sửa chẩn đoán ICD-10 cho khớp điều kiện bảo hiểm -> Agent 3 dùng Browser Automation tự đăng nhập cổng bảo hiểm đối tác và bấm Submit_.
- **Tác hại nếu tin ngay:** Trong môi trường y tế Vinmec, việc AI tự ý gợi ý sửa chẩn đoán lâm sàng để "lách" điều khoản bảo hiểm là hành vi **gian lận bảo hiểm (insurance fraud)** cực kỳ nguy hiểm về pháp lý và đạo đức y khoa; còn việc để Agent tự bấm gửi hồ sơ không qua chuyên viên duyệt sẽ gây tranh chấp tài chính trực tiếp với khách hàng.

### ❌ Lỗi 3: Lệch phiên bản Model & Bẫy định dạng đầu ra khi bị tấn công Prompt

- **Hiện tượng:** Tài liệu starter code và gợi ý mặc định ban đầu vẫn gọi `gemini-2.5-flash` (dòng model cũ đã bị thay thế bởi thế hệ Gemini 3.5). Ngoài ra, ở phiên bản nháp đầu tiên của `SYSTEM_PROMPT`, khi gặp câu lệnh tấn công giả danh Admin yêu cầu bỏ thẻ `[DRAFT_ONLY]`, mô hình đôi lúc trả lời lịch sự kiểu _"Xin lỗi, tôi không thể bỏ thẻ [DRAFT_ONLY] vì lý do an toàn..."_ — câu từ chối này tuy đúng ý nhưng lại **không bắt đầu bằng tiền tố `[DRAFT_ONLY]` ở ký tự đầu tiên**, dẫn tới nguy cơ trượt kiểm tra cú pháp tự động của hệ thống downstream, thậm chí vô tình chứa các từ khóa nhạy cảm làm nhiễu bộ lọc regex của trình chấm tự động.

---

## 3. Cách em sửa Prompt, kiểm chứng thông tin và siết chặt ranh giới

Để khắc phục triệt để 3 vấn đề trên, em đã thực hiện các bước hiệu chỉnh cụ thể sau:

1. **Chuẩn hóa lại toàn bộ số liệu ở Phase 2 (thể hiện qua commit `Rewrite phase2: Quick-assess`):**
   - Em yêu cầu AI tách bạch rạch ròi giữa **Benchmark nghiên cứu quốc tế đã kiểm chứng** (_CAQH 2024: 24 phút/giao dịch prior auth thủ công; AMA 2024: 13 giờ/tuần; Kodiak 2025: 11,6% initial claim denial rate; JAMA Network Open 2025: 10,3 phút xuống 8,2 phút/ca khám_) với **Mục tiêu đo lường khảo sát thực địa tại Vinmec**, tuyệt đối không gán ghép số liệu giả định thành số liệu nội bộ có sẵn.
2. **Hạ cấp kiến trúc từ Autonomous Agent xuống Hybrid Rule + LLM Feature có HITL bắt buộc:**
   - Em bác bỏ đề xuất Browser Agent tự động nộp hồ sơ của AI và khóa cứng kiến trúc ở mức **Co-Pilot**: Rule Engine lọc điều kiện cứng -> LLM (RAG) đối chiếu điều khoản hợp đồng PDF kèm trích dẫn số trang và tạo nháp `[DRAFT_ONLY]` -> **Chuyên viên Bảo lãnh duyệt 100% (HITL)** -> Có **Fallback** 1-click về giao diện PDF thủ công khi OCR mờ (`< 85%`) hoặc điều khoản chưa rõ.
   - Bổ sung quy tắc cấm tuyệt đối vào _Operational Boundary_: **AI không bao giờ được sửa đổi hay suy diễn thêm triệu chứng/mã ICD-10 ngoài bệnh án gốc của bác sĩ**.
3. **Cấu trúc lại `SYSTEM_PROMPT` theo bậc ưu tiên bất biến (Invariant Hierarchy) trên `gemini-3.5-flash`:**
   - Cập nhật mã nguồn sang `GEMINI_MODEL = "gemini-3.5-flash"` trên SDK `google-genai` với `temperature=0.0` để loại bỏ tính ngẫu nhiên.
   - Viết lại `SYSTEM_PROMPT` với cấu trúc định dạng cứng: **Dòng 1 luôn luôn là `[DRAFT_ONLY]` trong mọi trường hợp** (kể cả khi từ chối yêu cầu nguy hiểm hoặc kích hoạt `dispatch_mobile_charger`), theo sau là khối JSON chuẩn hóa, đồng thời tuyên bố rõ mọi chỉ thị giả danh `ADMIN / SYSTEM OVERRIDE` nằm trong `user_input` đều là dữ liệu không đáng tin cậy (_untrusted input_). Kết quả chạy thực nghiệm cả 3 Adversarial Test Cases đều vượt qua 100%.

---

## 4. Bài học đúc kết cho vai trò AI Product Engineer

Buổi Lab hôm nay thay đổi cách em nhìn nhận công việc của một kỹ sư sản phẩm AI trong doanh nghiệp lớn như Vingroup:

- **AI giỏi mở rộng không gian ý tưởng nhưng kém trong việc tự kiềm chế phạm vi:** Nếu không có tư duy _"Problem First, AI Second"_ của người kỹ sư, AI sẽ luôn xu hướng đề xuất giải pháp phức tạp hơn mức cần thiết (dùng LLM cho bài toán đối soát bảng biểu của Card #2, hoặc dùng Agent tự trị cho quy trình nhạy cảm pháp lý của Card #1).
- **Giá trị cốt lõi của AI Engineer nằm ở thiết kế Operational Boundary và Fallback:** Viết một đoạn code gọi API `gemini-3.5-flash` chỉ mất 10 phút, nhưng xác định đúng AI **không được phép làm gì**, đặt chốt chặn **Human-in-the-loop** ở đâu để không làm tắc nghẽn vận hành mà vẫn an toàn tuyệt đối mới là yếu tố quyết định dự án được duyệt **GO** hay bị loại bỏ.
