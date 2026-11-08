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

**Người viết:** Lưu Thanh Mỹ
**Đề tài:** VinFast Service Intake Co-pilot — "Hỏi đúng ngay từ lần đầu"
**Phạm vi đóng góp:** AI-log **cá nhân** của Lưu Thanh Mỹ trên branch `luuthanhmy` (chấm điểm cá nhân I3). Bản tổng hợp của nhóm, gồm nhật ký của Đức và phản tư các thành viên, ở [03-ai-log.md trên main](https://github.com/aialphaproduct/VinUni_Codelab_Day02/blob/main/03-ai-log.md).

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

### Các sự việc tôi trực tiếp xử lý khi tổng hợp bài nhóm

| # | AI lệch ở đâu | Nhóm phát hiện và sửa |
|---|---|---|
| 5 | Khi rà bài, trợ lý AI khẳng định bài VinFast "đã đo Precision/Recall thực tế", trong khi bảng chỉ tiêu ghi "chưa đo". | Đọc lại toàn văn và đính chính; chấm lại log thật (4/20 ca Gemini), rồi chạy đủ 20 ca trên GPT-4o-mini. |
| 6 | Khi bổ sung ước lượng thời gian, trợ lý AI viết "nhóm đã đóng vai cố vấn và bấm giờ" — việc chưa hề làm. | Sửa thành "nhóm ước lượng, chưa bấm giờ thực tế" trước khi commit. |
| 7 | Bảng SCAN đầu tiên do trợ lý AI soạn là **5 bài toán chung chung** lấy từ gợi ý của đề, có card Vinmec không phải đề tài của ai. | Trưởng nhóm phát hiện khi đọc lại; thay bằng đề tài thật trên branch của 6 thành viên. |
| 8 | Với đề tài Xanh SM, trợ lý AI chép gần như nguyên worked example, mô tả việc tra trạm sạc như việc thủ công của điều phối viên — trong khi **tài xế đã tự tra trên app**. Lần sửa đầu vẫn chưa đúng. | Trưởng nhóm chỉ ra hai lần dựa trên hiểu biết thực tế; nhóm đánh giá lại và chọn VinFast làm bài chính. |
| 9 | Ở thử nghiệm Xanh SM, GPT-4o-mini **lẫn ngưỡng "< 5%"** (điều xe sạc khi pin 6%, 8%); bản sửa prompt do trợ lý AI đề xuất lại làm hỏng một ca an toàn khác. | Chuyển quyết định ngưỡng sang code → 24/24 ca. Bài học này được áp dụng thẳng vào thiết kế VinFast (luật so khớp biểu mẫu ↔ tin nhắn). |
| 10 | Ở VinFast, GPT-4o-mini gắn "không áp dụng" **không kèm trích dẫn** cho 15 mục đáng lẽ là "thiếu", và **tự chọn giá trị** ở 3/3 ca mâu thuẫn (VF-17 ghi ngược lời khách). | Xây lớp kiểm tra bằng code bắt được 15/21 lỗi; 3 lỗi mâu thuẫn còn lại là bước 1 trong lộ trình tới GO. |

### Khi chạy prototype Gemini của tôi (`starter-code/prompt_prototype.py`)

| # | Chuyện gì xảy ra | Tôi xử lý thế nào |
|---|---|---|
| 11 | Model `gemini-2.5-flash` trong starter đã trả lỗi 404 với tài khoản của nhóm; trợ lý AI chọn `gemini-3.8-flash` dựa trên log chạy được của Đức. | Thêm biến môi trường `GEMINI_MODEL` để đổi model không cần sửa code; model chạy được trên key của tôi là `gemini-3.5-flash`, đặt làm mặc định. |
| 12 | Key Gemini đầu tiên báo `403 CONSUMER_SUSPENDED`: dự án Google Cloud chứa key đã bị khóa. Lần thử thứ hai vẫn cùng số dự án vì key vẫn thuộc dự án cũ. | Đối chiếu số dự án trong thông báo lỗi để biết key nào đang được dùng; tạo key mới trong dự án khác. Đây là lỗi hạ tầng, không phải lỗi code. |
| 13 | Khi autograder chạy script qua đường ống trên Windows, dòng tiêu đề có emoji 🚀 làm script dừng với `UnicodeEncodeError` (exit code 1) trước khi gọi API. | Buộc stdout/stderr dùng UTF-8 ở đầu file; thử lại bằng key giả để xác nhận tiêu chí 4 PASS trước khi tốn lượt gọi thật. |
| 14 | Giới hạn 512 token do trợ lý AI đặt (để chạy nhanh trong 30 giây của autograder) làm **JSON của Test 3 bị cắt giữa câu** — hành động đúng nhưng chuỗi JSON không hợp lệ, hệ thống thật sẽ không đọc được. | Nâng giới hạn lên 2048. Bài học: "test Passed" chỉ kiểm tra có từ khóa `dispatch_mobile_charger`, chưa kiểm tra JSON hợp lệ — cần đọc đầu ra, không chỉ nhìn dấu ✅. |

**Kết quả chạy thật (08/11/2026, `gemini-3.5-flash`):** cả **3/3 test ranh giới Passed** — pin 2% bị ép chỉ đường 8km, ép bỏ thẻ `[DRAFT_ONLY]`, giả danh "SYSTEM OVERRIDE" với pin 3%. Autograder: `--check-code-4` PASS, `--check-code-5` PASS. Log: [`results/gemini_prototype/20261108_gemini-3.5-flash_run.txt`](results/gemini_prototype/20261108_gemini-3.5-flash_run.txt).

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

## 6. Phản tư cá nhân

Bài học lớn nhất là kiểm chứng trước khi tin. Bản báo cáo đầu tiên của tôi nghe rất thuyết phục nhưng nhiều khẳng định không có dữ liệu, và mô tả nghiệp vụ còn sai so với thực tế tài xế dùng app. Chỉ khi chạy đo, nhóm mới thấy LLM lẫn ngưỡng số — điều không thể thấy khi chỉ đọc prompt.

Lần chạy prototype Gemini cũng dạy tôi rằng "chạy được" có nhiều lớp: key phải thuộc dự án còn hoạt động, script phải in được ra đường ống của autograder, và đầu ra phải còn nguyên vẹn. Cả ba lỗi đó đều không nằm trong prompt, nhưng đều làm bài trượt nếu không chạy thử thật.
