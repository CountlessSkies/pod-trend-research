---
name: "POD Trend Resources"
description: "Danh sách nguồn dữ liệu POD, phân loại theo vai trò và khả năng truy cập của AI."
---

## Phân vai nguồn dữ liệu

| Nhóm | Vai trò | Câu hỏi trả lời | Khi nào dùng |
|---|---|---|---|
| **A — Purchase Signal** | Kênh chính | *"Người ta đang tìm MUA gì trên POD?"* | Bắt buộc mỗi session |
| **B — Early Signal** | Kênh mở rộng | *"Gì đang nổi ngoài kia chưa kịp vào POD?"* | Khi Nhóm A chưa đủ 15 niche |
| **C — Validation** | Kênh xác nhận | *"Trend này có đủ volume thật không?"* | Khi cần xác nhận độ bền |

> ⚠️ **Quy tắc**: Mọi niche lấy từ Nhóm B **bắt buộc phải validate** lại bằng Nhóm A hoặc C trước khi đưa vào báo cáo.

---

## ✅ Nhóm A — Purchase Signal (Kênh chính)

AI có thể dùng `agent-browser` hoặc `web-search` với các nguồn này.

| # | Nguồn | URL | Ghi chú |
|---|---|---|---|
| 1 | **Insightfactory** | https://insightfactory.ai/redbubble-trends/ | Gold standard — keyword trends trực tiếp từ Redbubble |
| 2 | **TopBubbleIndex** | https://topbubbleindex.com/redbubble-popular-tags | Cross-validate với Insightfactory |
| 3 | **Podly** | https://podly.ai/tools/redbubble/trending-tags/ | Trending tags theo ngày |
| 4 | **BubbleScout** | https://bubblescout.com/ | Phân tích sâu hơn theo category |
| 5 | **Redbubble Popular Tags** | https://www.redbubble.com/found/popular-tags | Fallback khi các tool trên không truy cập được |

---

## 🔭 Nhóm B — Early Signal (Kênh tín hiệu sớm)

Phát hiện trend trước 3–6 tháng so với POD ecosystem. Kết quả phải validate lại qua Nhóm A.

| # | Nguồn | URL | Ghi chú |
|---|---|---|---|
| 6 | **Pinterest Predicts** | https://www.pinterestpredicts.com/ | Dự báo trend cả năm — aesthetic & lifestyle |
| 7 | **Pinterest Trends** | https://trends.pinterest.com/ | Volume tương đối theo thời gian, không phải số tuyệt đối |
| 8 | **Exploding Topics** | https://explodingtopics.com/ | Topic breakout trên internet nói chung |

> 💡 **Lưu ý**: Pinterest cho biết *gì đang được lưu/chia sẻ*, không phải *gì đang được mua*. Cần translate aesthetic trend → purchase keyword trước khi dùng.

---

## ✅ Nhóm C — Validation (Kênh xác nhận)

Dùng khi cần xác nhận volume hoặc xu hướng lên/xuống của một niche.

| # | Nguồn | URL | Ghi chú |
|---|---|---|---|
| 9 | **Google Trends** | https://trends.google.com/trends/ | So sánh tương đối, kiểm tra trend đang lên/flat/xuống |
| 10 | **KeywordTool.io (Pinterest)** | https://keywordtool.io/pinterest | Gợi ý từ khóa đuôi dài từ Pinterest search |
| 11 | **PinGroupie** | https://pingroupie.com/ | Board đang viral, mức tương tác |

---

## 🛡️ Nhóm TM — Trademark Check (Bước 2 riêng)

Dùng ở Bước 2 — Safety Check, không liên quan đến trend research.

| # | Nguồn | URL |
|---|---|---|
| 12 | **Trademarkia** | https://www.trademarkia.com/ |
| 13 | **USPTO** | https://tmsearch.uspto.gov/ |

---

## 🔒 Nhóm Paid — Requires Login / Paid Tool

AI **không thể** truy cập. Liệt kê để người dùng tham khảo thủ công.

| Tool | URL | Ghi chú |
|---|---|---|
| Pinterest Ads Keyword Tool | https://ads.pinterest.com/ | Vào Create Ad > Targeting — volume thật, cực mạnh |
| Minea | https://www.minea.com/ | Ad spy Pinterest/TikTok. Paid |
| AdSpy | https://adspy.com/ | Ad spy đa nền tảng. Paid |
