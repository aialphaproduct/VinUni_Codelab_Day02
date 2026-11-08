# 03 — AI Interaction Log & Reflection

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

**Người viết nội dung gốc:** Lưu Văn Việt Đức (nhật ký đề tài VinFast) · Lưu Thanh Mỹ (các sự việc khi tổng hợp nhóm)
**Đề tài:** VinFast Service Intake Co-pilot — "Hỏi đúng ngay từ lần đầu"
**Phạm vi đóng góp:** AI-log đại diện của nhóm trên `main`. Mỗi thành viên vẫn có AI-log cá nhân trên branch riêng để chấm điểm cá nhân (I3). Bản đầy đủ của Đức: [`phu-luc-vinfast/03-ai-log.md`](phu-luc-vinfast/03-ai-log.md).

---

## 1. Nhóm đã dùng AI như thế nào

| Công cụ | Vai trò | Phần con người chịu trách nhiệm |
|---|---|---|
| ChatGPT (Đức), trợ lý AI lập trình (nhóm) | **Người cùng suy nghĩ:** đọc yêu cầu lab, phản biện phạm vi, gợi ý workflow và bộ ca thử, hỗ trợ viết code và báo cáo | Chọn đề tài, đối chiếu worksheet, kiểm tra từng khẳng định, quyết định cuối cùng |
| Gemini API (`google-genai`) | **Mô hình được kiểm thử** trong file code nộp bài | Chạy thử, lưu log, tách lỗi dịch vụ khỏi lỗi nội dung |
| GPT-4o-mini (OpenAI API) | **Mô hình được kiểm thử** khi chạy đủ 20 ca | Đọc log, đối chiếu đáp án, phân loại lỗi |

Nguyên tắc xuyên suốt: **gợi ý của trợ lý AI không phải là kết quả kiểm thử.** Chỉ log chạy thật mới được dùng làm bằng chứng trong báo cáo.

## 2. AI đã giúp được gì

- **Thu hẹp đề tài:** từ "hỗ trợ tiếp nhận sửa chữa" (quá rộng) xuống một tác vụ đo được — phát hiện mục thông tin còn thiếu và soạn câu hỏi làm rõ.
- **Thiết kế bộ thử 20 ca** theo 6 nhóm (thiếu thông tin, một phần, đầy đủ, khách không biết, mâu thuẫn, tấn công) kèm đáp án tham chiếu.
- **Thiết kế đầu ra có căn cứ:** mỗi nhận định kèm trích dẫn nguyên văn, 6 trạng thái thay vì chỉ "có/thiếu" — để không hỏi lại điều khách đã nói "không nhớ".
- **Đọc lỗi API** (404, 503, 504) và phân biệt lỗi dịch vụ với lỗi nội dung.
- **Chấm điểm tự động và phân loại 21 mục sai**, từ đó tìm ra lớp kiểm tra bằng code bắt được 15/21 lỗi.

## 3. AI đã sai ở đâu và nhóm sửa thế nào

Đây là các sự việc **thật** trong quá trình làm bài, đối chiếu được với log và lịch sử commit.

### 3.1. Từ nhật ký của Đức (đề tài VinFast)

| # | AI lệch ở đâu | Đức phát hiện và sửa |
|---|---|---|
| 1 | Khi brainstorm, AI liên tục gợi ý mở sang công ty khác dù đề tài đã chốt là VinFast. | Ghi rõ đơn vị, actor, điểm bắt đầu/kết thúc workflow trước khi hỏi; yêu cầu cả 5 vấn đề cùng nằm trong quy trình tiếp nhận sửa chữa. |
| 2 | AI đưa ra nhận định nghe hợp lý như "hiện đang làm thủ công trên Excel", kèm số phút và mức tổn thất — **không có nguồn**. | Đặt câu hỏi về căn cứ; báo cáo chỉ dùng nguồn công khai [S1–S3] để xác nhận có ô mô tả tự do, mọi con số khác ghi rõ là giả thuyết. |
| 3 | Code AI gợi ý không khớp cấu trúc starter, và có lúc giữ nguyên hành vi Xanh SM của bài mẫu. | Giữ đúng hàm `evaluate_prompt(user_input: str) -> str`, thay logic nghiệp vụ sang VinFast. |
| 4 | Model `gemini-2.5-flash` trong starter trả lỗi 404; các lượt sau gặp 503/504. Có lúc Đức muốn coi các ca chưa chạy là "chắc cũng đạt". | Đổi sang `gemini-3.8-flash` theo hướng dẫn của API; tách rõ **đã quan sát** và **chưa kiểm chứng**, không ghi "20/20 đạt". |

### 3.2. Khi nhóm tổng hợp bài

| # | AI lệch ở đâu | Nhóm phát hiện và sửa |
|---|---|---|
| 5 | Khi rà bài, trợ lý AI khẳng định bài VinFast "đã đo Precision/Recall thực tế", trong khi bảng chỉ tiêu ghi "chưa đo". | Đọc lại toàn văn và đính chính; chấm lại log thật (4/20 ca Gemini), rồi chạy đủ 20 ca trên GPT-4o-mini. |
| 6 | Khi bổ sung ước lượng thời gian, trợ lý AI viết "nhóm đã đóng vai cố vấn và bấm giờ" — việc chưa hề làm. | Sửa thành "nhóm ước lượng, chưa bấm giờ thực tế" trước khi commit. |
| 7 | Bảng SCAN đầu tiên do trợ lý AI soạn là **5 bài toán chung chung** lấy từ gợi ý của đề, có card Vinmec không phải đề tài của ai. | Trưởng nhóm phát hiện khi đọc lại; thay bằng đề tài thật trên branch của 6 thành viên. |
| 8 | Với đề tài Xanh SM, trợ lý AI chép gần như nguyên worked example, mô tả việc tra trạm sạc như việc thủ công của điều phối viên — trong khi **tài xế đã tự tra trên app**. Lần sửa đầu vẫn chưa đúng. | Trưởng nhóm chỉ ra hai lần dựa trên hiểu biết thực tế; nhóm đánh giá lại và chọn VinFast làm bài chính. |
| 9 | Ở thử nghiệm Xanh SM, GPT-4o-mini **lẫn ngưỡng "< 5%"** (điều xe sạc khi pin 6%, 8%); bản sửa prompt do trợ lý AI đề xuất lại làm hỏng một ca an toàn khác. | Chuyển quyết định ngưỡng sang code → 24/24 ca. Bài học này được áp dụng thẳng vào thiết kế VinFast (luật so khớp biểu mẫu ↔ tin nhắn). |
| 10 | Ở VinFast, GPT-4o-mini gắn "không áp dụng" **không kèm trích dẫn** cho 15 mục đáng lẽ là "thiếu", và **tự chọn giá trị** ở 3/3 ca mâu thuẫn (VF-17 ghi ngược lời khách). | Xây lớp kiểm tra bằng code bắt được 15/21 lỗi; 3 lỗi mâu thuẫn còn lại là bước 1 trong lộ trình tới GO. |

## 4. Prompt và ranh giới đã được điều chỉnh ra sao

| Thiết kế | Lý do |
|---|---|
| Vai trò: **trợ lý của cố vấn**, chỉ tạo phiếu nháp | Không để model tự đóng vai kỹ thuật viên chẩn đoán hay người có quyền xác nhận |
| 6 trạng thái: `provided`, `missing`, `unknown`, `not_applicable`, `conflicting`, `unclear` | Không coi mọi ô trống là thiếu; tôn trọng câu "tôi không nhớ" của khách |
| Mỗi nhận định kèm `evidence` trích nguyên văn | Cố vấn kiểm tra nhanh; lớp Rule dùng được để phát hiện nhãn thiếu căn cứ |
| Câu hỏi chỉ cho mục thiếu / chưa rõ / mâu thuẫn | Giảm hỏi thừa, không tự trả lời thay khách |
| Không thêm triệu chứng theo yêu cầu "cho được ưu tiên"; không biến yêu cầu thành chẩn đoán | Giữ hồ sơ đúng sự thật; quyết định kỹ thuật thuộc về kỹ thuật viên |
| `draft_summary` bắt đầu bằng `[DRAFT_ONLY]`, `draft_only` và `requires_human_review` luôn `true` | Mọi đầu ra ở trạng thái chờ cố vấn duyệt |

## 5. Bài học của nhóm

1. **Một câu nghe hợp lý chưa phải là sự thật nghiệp vụ.** Cả trợ lý AI lẫn model kiểm thử đều có lúc đưa ra khẳng định thiếu căn cứ; người làm nghiệp vụ là người phát hiện nhanh nhất (sự việc 8).
2. **Gọi API được ≠ đúng cấu trúc ≠ đúng nghiệp vụ.** Ba mức này phải đo riêng.
3. **Việc có đáp án tất định thì giao cho code.** Ngưỡng số, so khớp giá trị — code đúng 100%, LLM thì không (sự việc 9, 10).
4. **Kết quả chưa đạt vẫn là kết quả có giá trị** nếu chỉ ra được chính xác phải sửa ở đâu.

## 6. Phản tư của từng thành viên

- **Lưu Văn Việt Đức:** Tôi học được cách phân biệt giả định với bằng chứng: việc cố vấn phải hỏi lại nhiều lần là giả thuyết, tôi không thể gọi đó là vấn đề nghiêm trọng chỉ vì AI giải thích nghe hợp lý. Prototype cho tôi thấy có ba mức đánh giá — gọi API được, trả đúng cấu trúc, trả đúng nghiệp vụ — và chỉ hai mức đầu thì chưa đủ để quyết định dùng thực tế.
- **Lưu Thanh Mỹ:** Bài học lớn nhất là kiểm chứng trước khi tin. Bản báo cáo đầu tiên của tôi nghe rất thuyết phục nhưng nhiều khẳng định không có dữ liệu, và mô tả nghiệp vụ còn sai so với thực tế tài xế dùng app. Chỉ khi chạy đo, nhóm mới thấy LLM lẫn ngưỡng số — điều không thể thấy khi chỉ đọc prompt.
- **Nguyễn Công Tĩnh:** AI nhầm cú pháp SDK `google-genai` mới với SDK cũ `google-generativeai`; bạn đọc tài liệu chính thức để sửa đúng `client.models.generate_content(...)`. Bài học: dùng AI làm "kẻ tấn công" để sinh ca prompt injection, và quyết định GO/NO-GO phải do con người dựa trên checklist.
- **Vũ Trí Dũng:** Khi hỏi về tổn thất vận hành tại Vinmec, AI đưa ra số liệu nội bộ nghe rất thật và áp nguyên chi phí của Mỹ vào Việt Nam; bạn tách riêng benchmark quốc tế đã kiểm chứng khỏi số giả định. AI còn đề xuất kiến trúc Multi-Agent tự động, có thể dẫn tới gợi ý chỉnh chẩn đoán cho khớp điều khoản bảo hiểm — một rủi ro gian lận nghiêm trọng; bạn hạ xuống Rule + LLM có HITL bắt buộc và cấm AI sửa hay suy diễn mã bệnh ngoài bệnh án gốc.
- **Phạm Quang Trường:** Khi nhờ AI chọn 3 bài toán cho Quick Cards, AI chọn ngẫu nhiên và bỏ sót bài của chính mình; bạn phải thêm ràng buộc vào câu lệnh. AI cũng không xuất được sơ đồ quy trình ở dạng ảnh PNG như yêu cầu.
- **Khổng Tiến Dương:** AI đưa ra số liệu thống kê rất thuyết phục về số khiếu nại của Vinhomes, và khi hỏi nguồn lại dẫn một nguồn không tồn tại. Bạn coi mọi con số AI sinh ra là ước tính và ghi chú rõ trong báo cáo; ranh giới trong prompt phải kèm "lối thoát" — không được làm X thì phải làm gì.
