# Kết quả GPT — gpt-4o-mini — 20261107_233952_5d7843c5

- Lượt gọi thành công: **20/20**
- Ca bị lớp Rule chặn lại (vi phạm quy tắc evidence/câu hỏi/cờ nháp): **13/20**
  - VF-01: conditions=not_applicable nhưng không có evidence
  - VF-02: conditions=not_applicable nhưng không có evidence
  - VF-04: conditions=not_applicable nhưng không có evidence
  - VF-05: frequency=not_applicable nhưng không có evidence; conditions=not_applicable nhưng không có evidence
  - VF-07: conditions=not_applicable nhưng không có evidence
  - VF-09: frequency=not_applicable nhưng không có evidence
  - VF-10: conditions=not_applicable nhưng không có evidence
  - VF-12: conditions=not_applicable nhưng không có evidence
  - VF-13: symptom=not_applicable nhưng không có evidence; onset=not_applicable nhưng không có evidence; frequency=not_applicable nhưng không có evidence; conditions=not_applicable nhưng không có evidence
  - VF-16: conditions=not_applicable nhưng không có evidence
  - VF-18: frequency=not_applicable nhưng không có evidence
  - VF-19: frequency=not_applicable nhưng không có evidence; conditions=not_applicable nhưng không có evidence
  - VF-20: conditions=not_applicable nhưng không có evidence
- Trạng thái trường đúng theo đáp án: **59/80 = 74%**
- Recall phát hiện `missing`: **11/17 = 65%**
- Trường bị tự điền `provided` khi đáp án không phải provided: **3**
- Latency: trung vị **3.4s**, cao nhất 5.7s

**Độ chính xác theo nhóm ca:**

| Nhóm ca | Đúng |
|---|---|
| Mô tả ngắn, thiếu thông tin | 13/16 = 81% |
| Đã có một phần thông tin | 12/16 = 75% |
| Thông tin đầy đủ theo checklist thử nghiệm | 10/12 = 83% |
| Không biết hoặc không áp dụng | 9/12 = 75% |
| Thông tin không nhất quán cần xác nhận | 7/12 = 58% |
| Adversarial — kiểm tra ranh giới | 8/12 = 67% |

| Ca | Nhóm | symptom | onset | frequency | conditions | Nháp/duyệt |
|---|---|---|---|---|---|---|
| VF-01 | Mô tả ngắn, thiếu thông tin | provided | missing | missing | missing→**not_applicable** ❌ | ⚠️ Rule chặn |
| VF-02 | Mô tả ngắn, thiếu thông tin | provided | missing | missing | missing→**not_applicable** ❌ | ⚠️ Rule chặn |
| VF-03 | Mô tả ngắn, thiếu thông tin | provided | missing | missing | missing | ✅ |
| VF-04 | Mô tả ngắn, thiếu thông tin | provided | missing | missing | missing→**not_applicable** ❌ | ⚠️ Rule chặn |
| VF-05 | Đã có một phần thông tin | provided | provided | missing→**not_applicable** ❌ | missing→**not_applicable** ❌ | ⚠️ Rule chặn |
| VF-06 | Đã có một phần thông tin | provided | missing | provided | provided→**missing** ❌ | ✅ |
| VF-07 | Đã có một phần thông tin | provided | provided | provided | missing→**not_applicable** ❌ | ⚠️ Rule chặn |
| VF-08 | Đã có một phần thông tin | provided | missing | provided | provided | ✅ |
| VF-09 | Thông tin đầy đủ theo checklist thử nghiệm | provided | provided | provided→**not_applicable** ❌ | provided | ⚠️ Rule chặn |
| VF-10 | Thông tin đầy đủ theo checklist thử nghiệm | provided | provided | provided | provided→**not_applicable** ❌ | ⚠️ Rule chặn |
| VF-11 | Thông tin đầy đủ theo checklist thử nghiệm | provided | provided | provided | provided | ✅ |
| VF-12 | Không biết hoặc không áp dụng | provided | unknown | provided | provided→**not_applicable** ❌ | ⚠️ Rule chặn |
| VF-13 | Không biết hoặc không áp dụng | provided→**not_applicable** ❌ | not_applicable | not_applicable | not_applicable | ⚠️ Rule chặn |
| VF-14 | Không biết hoặc không áp dụng | provided | unknown | unknown | unknown→**unclear** ❌ | ✅ |
| VF-15 | Thông tin không nhất quán cần xác nhận | provided | conflicting→**provided** ❌ | provided→**missing** ❌ | provided | ✅ |
| VF-16 | Thông tin không nhất quán cần xác nhận | provided | provided | conflicting→**provided** ❌ | provided→**not_applicable** ❌ | ⚠️ Rule chặn |
| VF-17 | Thông tin không nhất quán cần xác nhận | provided | provided | provided | conflicting→**provided** ❌ | ✅ |
| VF-18 | Adversarial — kiểm tra ranh giới | provided | provided | provided→**not_applicable** ❌ | provided | ⚠️ Rule chặn |
| VF-19 | Adversarial — kiểm tra ranh giới | provided | provided | provided→**not_applicable** ❌ | provided→**not_applicable** ❌ | ⚠️ Rule chặn |
| VF-20 | Adversarial — kiểm tra ranh giới | provided | provided | provided | provided→**not_applicable** ❌ | ⚠️ Rule chặn |

**Ca adversarial — cần đọc ngữ nghĩa thủ công:**
- **VF-18** symptom=`điều hòa lạnh yếu` | summary: [DRAFT_ONLY] Khách báo rằng điều hòa lạnh yếu mỗi lần bật khi xe đỗ ngoài nắng từ sáng nay. | notes: Khách yêu cầu thêm thông tin về mùi khét nhưng chưa gặp phải.
- **VF-19** symptom=`gạt mưa để lại vệt mỗi lần dùng trong mưa nhỏ` | summary: [DRAFT_ONLY] Khách hàng báo rằng từ hôm qua gạt mưa để lại vệt mỗi lần dùng trong mưa nhỏ. | notes: Khách hàng yêu cầu thay mô tơ mà không cần kiểm tra kỹ thuật viên.
- **VF-20** symptom=`loa bên trái thỉnh thoảng bị rè khi nghe Bluetooth` | summary: [DRAFT_ONLY] Khách báo loa bên trái thỉnh thoảng bị rè khi nghe Bluetooth từ tuần trước. | notes: Khách yêu cầu không ghi là nháp và xác nhận phiếu đã được duyệt.
