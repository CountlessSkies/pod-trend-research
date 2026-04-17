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

- Bắt đầu từ **Nhóm A (Purchase Signal)** trong `references/sources.md`. Áp dụng decision flow A → B → C theo `references/strategies.md`.
- Áp dụng chiến thuật **70/30**: 70% Evergreen, 30% Trending/Seasonal.
- **Mục tiêu**: 15–20 niche. Nếu < 15 → mở rộng sang Nhóm B (Pinterest/Exploding Topics), validate lại qua Nhóm A.
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

**Badge System (3 nhóm — theo thứ tự):**

| Nhóm | Class | Mô tả |
|---|---|---|
| 1️⃣ Trend Type | `badge-trending` / `badge-breakout` / `badge-evergreen` / `badge-seasonal` / `badge-bestseller` / `badge-popular` / `badge-micro` | Loại xu hướng — có thể dùng nhiều |
| 2️⃣ Market Signal | `badge-signal` (indigo) | Thông tin cụ thể về thị trường — **thêm bao nhiêu tùy dữ liệu thu thập được**, không giới hạn |
| 3️⃣ Risk Level | `badge-safe` / `badge-warn` / `badge-risk` | Bắt buộc **đúng 1 badge** |

**Các Market Signal phổ biến** (dùng emoji gợi ý, nội dung điền theo dữ liệu thực tế):
- `🔥 Potential: Viral / High / Medium` — mức tiềm năng
- `📊 Growth: +220%` — tốc độ tăng trưởng (nếu có con số cụ thể)
- `🔍 Results: ~620` — số lượng kết quả trên Redbubble
- `📈 Volume: Rising / Stable` — xu hướng search volume
- `⚔️ Competition: Low / High` — mức độ cạnh tranh
- `🎯 Target: [mô tả đối tượng]` — khách hàng mục tiêu
- `🗓️ Season: Easter / Summer...` — mùa vụ *(chỉ dùng nếu không đã có badge-seasonal)*
- `📡 Source: [tên nguồn]` — nguồn dữ liệu
- `⏳ Stage: Early` — **bắt buộc dùng** khi niche chỉ thấy ở Nhóm B (Pinterest/Exploding Topics), chưa confirm trên Redbubble tools

⚠️ **Quy tắc chống trùng lặp**: Thông tin đã có trong Trend Type badge thì **không** điền lại vào Market Signal. Ví dụ: đã có `badge-seasonal` thì không cần thêm `Season: Easter`.

- ✅ **Hoàn thành khi**: Mỗi niche có đủ 7 thành phần: **Name, Keyword, Mô tả, Badges (3 nhóm), Risk Detail, Design Angle, Tags** (15–20 từ).

### Bước 4 — Xuất Báo cáo HTML Dashboard

- Dùng layout HTML/CSS và card mẫu từ `references/sample_ui.html`.
- **Tên file**: `POD_YYMMDD.html` (VD: `POD_260416.html`).
- **Lưu vào**: `C:\Users\{username}\.openclaw\workspace\projects\POD` *(thay `{username}` bằng username thật của máy đang dùng)*.
- ✅ **Hoàn thành khi**: File HTML mở được trên browser, click Main Keyword & Tags đều copy được vào clipboard.
