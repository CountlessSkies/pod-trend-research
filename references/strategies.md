---
name: "POD Research Strategies"
description: "Quy tắc tìm kiếm, làm giàu dữ liệu và kiểm tra an toàn cho POD."
---

## 🗂️ Chiến lược chọn nguồn (Source Strategy)

**Luôn bắt đầu từ Nhóm A**, nhưng không bỏ qua Nhóm B dù đã đủ số lượng:

```
Bắt đầu → Nhóm A (Purchase Signal — Redbubble ecosystem)
               ↓
          Thu thập tất cả niche tìm được
               ↓
          Nhóm B (Early Signal — Pinterest / Exploding Topics)
               │  Nếu có breakout đáng chú ý → thêm vào dù Nhóm A đã đủ
               │  Label: Stage: Early + Source: [tên nguồn]
               ↓
          Nhóm C (Validation — tùy chọn)
               │  Dùng khi cần xác nhận độ bền / volume của bất kỳ niche nào
```

- **Nhóm A** → đưa thẳng vào báo cáo, confidence cao
- **Nhóm B** → đưa vào báo cáo, label `⏳ Stage: Early` để người dùng biết là tín hiệu sớm
- **Nhóm C** → không discovery, chỉ dùng để bổ sung thông tin validation

> 💡 **Triết lý**: Đây là **báo cáo tình báo thị trường**, không phải kế hoạch hành động. Càng nhiều tín hiệu càng tốt — kể cả chưa được xác nhận. Label confidence là công cụ để người dùng tự đánh giá, không phải để AI lọc thay. Chỉ loại bỏ khi AI tự bịa hoàn toàn không có nguồn.
>
> **AI không phải là người ra quyết định kinh doanh.** Nhiệm vụ của skill là cung cấp đầy đủ thông tin và label rõ confidence — kể cả những tín hiệu chưa được xác nhận.

---

## 🔍 Chiến thuật thu thập (Search Strategy)
- **Hạn chế quét trực tiếp**: Tuyệt đối không quét trực tiếp Redbubble với tần suất cao. Ưu tiên lấy "Seed Keywords" từ các công cụ bên thứ 3.
- **Làm giàu dữ liệu (Data Enrichment)**: Nếu nguồn chính thiếu thông tin, bắt buộc sử dụng `web-search` hoặc `agent-browser` để tìm hiểu thêm về:
    - **Target Audience**: Họ là ai? (Vd: Giáo viên mầm non, người yêu mèo, Gen Z...)
    - **Niche Context**: Tại sao nó đang hot? Có sự kiện nào đang diễn ra không?
    - **Design Insight**: Các mẫu đang bán chạy có đặc điểm gì chung?

## 🛡️ Kiểm tra an toàn (Safety & Trademark)
- **Tra cứu bắt buộc**: Mọi Keyword chính phải được kiểm tra qua Trademarkia hoặc USPTO.
- **Phân loại rủi ro**:
    - **Safe**: Không tìm thấy Trademark liên quan đến ngành hàng may mặc/phụ kiện.
    - **Warning**: Có Trademark nhưng thuộc ngành khác, hoặc là cụm từ phổ thông nhưng cần cẩn trọng.
    - **Copyright**: Rõ ràng là thương hiệu phim, nhạc, game hoặc cụm từ đã đăng ký bản quyền cho quần áo.
- **Nguyên tắc**: Không bỏ qua Copyright, nhưng phải ghi chú cực kỳ chi tiết chủ sở hữu IP để người dùng biết mà tránh hoặc "lách" sang sub-niche an toàn.

## 💡 Tư duy chọn Niche
- Ưu tiên các niche có **Search Volume cao** nhưng **Result count < 1000** (Micro-Niche).
- Tìm kiếm các "Keyword giao thoa" (Cross-niche). Vd: "Cat mom" + "Teacher".
