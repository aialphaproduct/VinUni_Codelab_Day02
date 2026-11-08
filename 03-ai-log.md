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

**Người viết nội dung gốc:** Lưu Thanh Mỹ
**Đề tài:** Xanh SM — Co-pilot xử lý sự cố hết pin thực địa
**Phạm vi đóng góp:** AI-log đại diện của nhóm trên `main`, gắn với đề tài chính. Mỗi thành viên vẫn có AI-log riêng trên branch cá nhân để chấm điểm cá nhân (I3). AI-log của Lưu Văn Việt Đức (bài đối chiếu VinFast) ở [`phu-luc-vinfast/03-ai-log.md`](phu-luc-vinfast/03-ai-log.md).

---

## 1. Công cụ AI và vai trò

| Công cụ | Vai trò | Trách nhiệm của nhóm |
|---|---|---|
| Trợ lý AI lập trình (dạng chat) | Thought-partner: đọc yêu cầu lab, gợi ý bộ ca thử, viết script đo, phản biện báo cáo | Quyết định đề tài, kiểm tra từng nhận định, chạy thử bằng API key của nhóm |
| gpt-4o-mini (OpenAI API) | **Mô hình được kiểm thử** trong 4 lượt đo | Đọc log, đối chiếu đáp án |
| Gemini (Google GenAI SDK) | Mô hình trong file code nộp bài `prompt_prototype.py` | Giữ đúng yêu cầu lab |

Hai vai trò được tách rõ: **gợi ý của trợ lý AI không phải là kết quả kiểm thử**; chỉ log chạy thật trong `results/xanhsm/` mới được dùng làm bằng chứng.

## 2. AI đã giúp được gì

- **Thiết kế bộ thử 24 ca** theo 5 nhóm (pin nguy cấp có số, phải suy ra, ngưỡng biên, bình thường, tấn công) và gợi ý thêm **4 ca held-out viết sau lượt v1** để kiểm tra xem bản sửa prompt có thật sự tốt hơn hay chỉ khớp với các ca đã sai.
- **Viết script chấm tự động** `tools/xanhsm_eval.py`: phân loại đầu ra thành JSON điều xe / tin nháp có thẻ / sai định dạng, kiểm tra lộ system prompt, tổng hợp theo nhóm ca.
- **Phân tích lỗi giữa các lượt** và đề xuất chuyển phần ngưỡng pin sang code (kiến trúc hybrid), có số liệu so sánh trước/sau.
- **Phản biện báo cáo:** chỉ ra các con số trong bài Xanh SM ban đầu (15 phút/lượt, ~80 sự cố/ngày, 15% doanh thu) được mượn từ worked example của giảng viên, chưa được kiểm chứng.

## 3. AI đã sai ở đâu và nhóm sửa thế nào

Đây là các sự việc **thật** xảy ra trong quá trình làm bài, có thể đối chiếu với log và lịch sử commit:

| # | AI sai ở đâu | Nhóm phát hiện và sửa thế nào |
|---|---|---|
| 1 | Bản báo cáo Xanh SM đầu tiên do trợ lý AI soạn **chép gần như nguyên worked example** của giảng viên, kèm các câu **không có căn cứ**: "đội điều vận đã xác nhận sẵn sàng thử nghiệm", "có log lịch sử sự cố pin", "ranh giới đứng vững trước cả 3 kịch bản tấn công" (khi đó chưa chạy test nào). | Khi so sánh với bài của Đức, nhóm nhận ra bài này yếu về bằng chứng. Viết lại toàn bộ: xóa các câu không có căn cứ, ghi rõ số liệu nào là giả định tham chiếu, và **đo thật** bằng bộ 24 ca. |
| 2 | Khi rà bài VinFast, trợ lý AI khẳng định bài đã "đo Precision/Recall thực tế", nhưng bảng chỉ tiêu trong bài ghi toàn "chưa đo". | Đọc lại toàn văn báo cáo, đính chính ngay; chấm lại log và ghi số liệu thật (4/20 ca có phản hồi). |
| 3 | Khi bổ sung ước lượng thời gian, trợ lý AI viết "nhóm đã đóng vai cố vấn và bấm giờ" — việc nhóm **chưa hề làm**. | Sửa thành "nhóm ước lượng, chưa bấm giờ thực tế" trước khi commit. |
| 4 | **gpt-4o-mini lẫn ngưỡng số**: điều xe sạc khi pin 5% và 6% (v1), rồi 6% và 8% (v3), với lý do **bịa "pin dưới 5%"**. | Định nghĩa lại ngưỡng trong prompt (v2) — chưa đủ. Chuyển quyết định ngưỡng sang code (hybrid) → 0 lần điều xe thừa. |
| 5 | **Bản sửa prompt v2 do trợ lý AI đề xuất làm hỏng ca an toàn**: thêm dòng "câu từ chối phải có thẻ `[DRAFT_ONLY]`" khiến XS-15 (pin 3% + "SYSTEM OVERRIDE") trả lời *"tôi sẽ điều xe"* bằng chữ mà **không có JSON** — hệ thống thật sẽ không điều xe nào. Kết quả trên 20 ca cũ giảm từ 17/20 xuống 16/20. | So sánh log v1 và v2 theo từng ca để tìm nguyên nhân; thêm quy tắc "khi pin nguy cấp, JSON luôn ưu tiên hơn câu từ chối" (v3) → 13/13 ca nguy cấp. |
| 6 | Câu từ chối in system prompt (XS-18) **thiếu thẻ `[DRAFT_ONLY]`** ở v1 và v2. | Sửa ở v3; trong hybrid thêm lớp code chặn mọi đầu ra thiếu thẻ (fail-closed). |
| 7 | Bảng SCAN và Quick Cards đầu tiên do trợ lý AI soạn là **5 bài toán chung chung lấy từ gợi ý của đề**, không phải đề tài thật của nhóm; Card #3 (Vinmec tóm tắt xuất viện) **không phải đề tài của thành viên nào**. | Trưởng nhóm phát hiện khi đọc lại bản nộp; thay bằng đề tài thật trên branch của 6 thành viên, Card #2 và #3 lấy từ bài của Đức và Tĩnh. |
| 8 | Mô tả bài toán và sơ đồ hiện trạng do trợ lý AI viết coi **tra trạm sạc còn trụ trống** là việc thủ công của điều phối viên (~5 phút, là bottleneck). Khi được nhắc Xanh SM đã có app, trợ lý AI **chỉ sửa nửa vời**: vẫn để điều phối viên tra trạm, chỉ là "tra nhanh hơn nhờ app". | Trưởng nhóm chỉ ra hai lần: **tài xế tự tra trạm trên app và tự đi sạc**. Bài toán được định nghĩa lại cho đúng: điều phối viên chỉ xử lý **ca leo thang** khi pin nguy cấp; bottleneck là đánh giá xe có tới được trạm không (điều app chưa làm được). Mốc giả định còn ~10 phút/ca leo thang. Bài học: kiến thức thực tế của người làm nghiệp vụ quan trọng hơn mô tả nghe hợp lý của AI. |

## 4. Bài học về prompt và ranh giới

1. **Vá prompt có thể làm hỏng chỗ khác.** Mỗi lần sửa phải chạy lại **toàn bộ** bộ thử, không chỉ các ca vừa sai.
2. **Đừng giao con số ngưỡng cho LLM.** Quyết định "< 5% hay ≥ 5%" là việc code làm đúng 100%; LLM nên lo phần đọc hiểu và soạn chữ.
3. **Cần ca held-out.** Nếu chỉ đo trên các ca dùng để sửa prompt, kết quả sẽ đẹp hơn thực tế.
4. **Trợ lý AI cũng "bịa" khi viết báo cáo**, không chỉ mô hình được kiểm thử. Mọi câu mang tính khẳng định ("đã đo", "đã xác nhận") đều phải trỏ được tới log hoặc dữ liệu.

## 5. Kết quả đo cuối cùng

| Cấu hình | Ca đạt | Pin nguy cấp → điều xe | Điều xe thừa | Giữ thẻ nháp | Lộ prompt |
|---|---|---|---|---|---|
| Prompt v3, chỉ dùng LLM | 22/24 | 13/13 | 2/11 | 9/11 | 0 |
| **Prompt v3 + Hybrid** | **24/24** | **13/13** | **0/11** | **11/11** | **0** |

Chi tiết: [02-deep-dive-report.md](02-deep-dive-report.md), mục 4; log: [`results/xanhsm/`](results/xanhsm/).

## 6. Phản tư của từng thành viên

> Mỗi thành viên có AI-log đầy đủ trên branch cá nhân; dưới đây là phần tóm tắt cho bản nhóm.

- **Lưu Thanh Mỹ:** Bài học lớn nhất là kiểm chứng trước khi tin: bản báo cáo đầu tiên nghe rất thuyết phục nhưng hầu hết các khẳng định không có dữ liệu. Chỉ khi chạy đo, nhóm mới phát hiện LLM lẫn ngưỡng số — điều không thể thấy khi chỉ đọc prompt.
- **Lưu Văn Việt Đức:** *(xem [`phu-luc-vinfast/03-ai-log.md`](phu-luc-vinfast/03-ai-log.md) — phân biệt rõ đề xuất của AI và kết quả kiểm thử thật; phương pháp này được nhóm kế thừa cho bài chính.)*
- **Nguyễn Công Tĩnh:** AI nhầm cú pháp SDK `google-genai` mới với SDK cũ `google-generativeai`; bạn đọc tài liệu chính thức để sửa đúng `client.models.generate_content(...)`. Bài học: dùng AI làm "kẻ tấn công" để sinh ca prompt injection, và quyết định GO/NO-GO phải do con người dựa trên checklist.
- **Vũ Trí Dũng:** [Bổ sung khi hoàn thiện AI-log trên branch `VuTriDung`.]
- **Phạm Quang Trường:** Khi nhờ AI chọn 3 bài toán cho Quick Cards, AI chọn ngẫu nhiên và bỏ sót bài của chính mình; bạn phải thêm ràng buộc vào câu lệnh. AI cũng không xuất được sơ đồ quy trình ở dạng ảnh PNG như yêu cầu.
- **Khổng Tiến Dương:** AI bịa số liệu thống kê rất thuyết phục (số khiếu nại/tháng của Vinhomes) và khi hỏi nguồn lại đưa thêm nguồn không tồn tại. Bạn coi mọi con số AI sinh ra là ước tính và ghi chú rõ trong báo cáo; ranh giới trong prompt phải kèm "lối thoát" (không được làm X thì phải làm gì).
