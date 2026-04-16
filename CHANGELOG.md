# Changelog

Mọi thay đổi đáng kể của skill này được ghi lại tại đây.

---

## [1.2.2] — 2026-04-16

### Changed
- **`references/templates.md`** + **`samples/POD_sample_output.md`** → gộp thành **`references/sample_ui.html`**.
- Lý do: OpenClaw đọc `.html` trực tiếp để hiểu chính xác cấu trúc tag và class — tránh sai lệch khi render markdown có chứa HTML.
- `references/sample_ui.html` gồm: full CSS, toàn bộ HTML boilerplate với `{{PLACEHOLDER}}`, và 3 card mẫu (Safe / Warning / Copyright) nằm trong comment để tham khảo.
- Cập nhật `SKILL.md`: Document Map giờ chỉ còn 3 dòng references.

---

## [1.2.1] — 2026-04-16

### Changed
- **`samples/POD_sample_output.html`** → đổi sang **`samples/POD_sample_output.md`**: OpenClaw ưu tiên `.md`. HTML mẫu giờ nằm trong code block bên trong file markdown.

---

## [1.2.0] — 2026-04-16

### Changed
- **`SKILL.md`**: Refactored toàn bộ. Xóa mô tả badge/card/CSS trùng lặp. File nay chỉ là navigation map + workflow + decision tree.
- **`references/sources.md`**: Chia thành 2 nhóm rõ ràng: ✅ AI-Accessible và 🔒 Requires Login/Paid. Sắp xếp lại thứ tự ưu tiên nguồn Primary.

### Added
- **Decision Tree** cho Safety Check trong `SKILL.md` — rõ ràng hóa logic phân loại badge-safe / badge-warn / badge-risk.
- **"Hoàn thành khi" (Done Criteria)** cho mỗi bước workflow trong `SKILL.md`.
- **`samples/POD_sample_output.html`**: File output mẫu hoàn chỉnh để AI calibrate chất lượng.
- **`CHANGELOG.md`**: File này.

### Removed
- **`samples/card_template.html`**: Xóa. OpenClaw ưu tiên `.md`. Template HTML đầy đủ đã có trong `references/templates.md`.

### Fixed
- `card_template.html` dùng class CSS sai (`badge-trend` thay vì `badge-trending`). Đã xóa file.
- Output path hardcode tên user cụ thể `Meander` → thay bằng placeholder `{username}`.

---

## [1.1.0] — 2026-04-10

### Added
- Cấu trúc skill ban đầu: `SKILL.md`, `references/`, `scripts/`, `samples/`.
- `references/sources.md`, `references/strategies.md`, `references/templates.md`.
- `scripts/check_tm.py`.
- `samples/card_template.html`.
