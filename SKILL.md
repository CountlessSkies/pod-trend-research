---
name: "POD Trend Researcher"
description: "Chuyên gia nghiên cứu trend POD đa kênh qua bên thứ 3 và xuất báo cáo HTML Dashboard chuyên nghiệp."
---

## 📌 Điều hướng Tài liệu (Document Map)

> Đây là file điều hướng. Toàn bộ chi tiết kỹ thuật nằm ở `references/`. **Không** tự suy hay tự bịa ngoài phạm vi các file dưới đây.

| Cần gì? | Đọc file nào? |
|---|---|
| Danh sách nguồn dữ liệu | `references/sources.md` |
| Chiến thuật lọc niche, Safety Check | `references/strategies.md` |
| HTML/CSS layout, class badge, card mẫu | `references/sample_ui.html` |

---

## 🛠️ Công cụ Automation

- **Kiểm tra Trademark nhanh**: Chạy `python scripts/check_tm.py "keyword"` → trả về link Trademarkia để tra thủ công.
- ⚠️ **Lưu ý quan trọng**: Script này chỉ **generate link**, không tự check. Phải dùng `agent-browser` để mở link và đọc kết quả thật.

---

## ⚙️ Quy trình (Workflow)

### Bước 1 — Sàng lọc Trend (Scoping)

- Truy cập các nguồn **AI-Accessible** (Nhóm 1) trong `references/sources.md`.
- Áp dụng chiến thuật **70/30** từ `references/strategies.md`: 70% Evergreen, 30% Trending/Seasonal.
- **Mục tiêu**: 15–20 niche. Nếu < 10 tìm được → mở rộng sang nguồn Secondary trong cùng file.
- ✅ **Hoàn thành khi**: Có danh sách raw keywords với tên niche + nguồn lấy từ đâu.

### Bước 2 — Safety Check (Kiểm tra Trademark)

Với **mỗi** Main Keyword, áp dụng Decision Tree:

```
Có Trademark trong ngành May mặc / Phụ kiện?
│
├── KHÔNG → 🟢 Safe
│           Badge: badge-safe
│
├── CÓ — Thuộc ngành khác HOẶC cụm từ phổ thông → 🟡 Warning
│         Badge: badge-warn
│         → Ghi rõ lý do vào trường "Chi tiết rủi ro"
│
└── CÓ — Rõ ràng là IP (phim, nhạc, game, brand lớn) → 🔴 Copyright
          Badge: badge-risk
          → Ghi tên chủ sở hữu IP + gợi ý sub-niche lách (nếu có)
```

⚠️ **Không bỏ niche nào**. Kể cả Copyright vẫn giữ lại trong báo cáo, chỉ gắn badge đúng.

### Bước 3 — Phân tích & Data Enrichment

- Xác định: Niche Name, Main Keyword, Target Audience, Design Angle.
- Nếu thiếu thông tin: dùng `agent-browser` vào Pinterest hoặc Insightfactory để bổ sung.
- Chi tiết chiến thuật: xem `references/strategies.md`.
- ✅ **Hoàn thành khi**: Mỗi niche có đủ 6 trường: **Name, Keyword, Mô tả, Risk Level, Design Angle, Tags** (15–20 từ).

### Bước 4 — Xuất Báo cáo HTML Dashboard

- Dùng layout HTML/CSS và card mẫu từ `references/sample_ui.html`.
- **Tên file**: `POD_YYMMDD.html` (VD: `POD_260416.html`).
- **Lưu vào**: `C:\Users\{username}\.openclaw\workspace\projects\POD` *(thay `{username}` bằng username thật của máy đang dùng)*.
- ✅ **Hoàn thành khi**: File HTML mở được trên browser, click Main Keyword & Tags đều copy được vào clipboard.
