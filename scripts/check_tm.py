import sys

def check_trademark(keyword):
    """
    Trả về link tra cứu Trademark nhanh cho AI/người dùng mở thủ công.

    Lưu ý USPTO: Hệ thống mới (thay thế TESS từ 11/2023) là SPA,
    không hỗ trợ deep-link qua URL param. Cần nhập keyword tay trên trang.
    """
    safe_kw = keyword.replace(' ', '+')
    trademarkia_url = f"https://www.trademarkia.com/trademarks-search.aspx?tn={safe_kw}"
    uspto_url = "https://tmsearch.uspto.gov/"  # SPA — nhập keyword tay tại đây

    print(f"Keyword    : {keyword}")
    print(f"Trademarkia: {trademarkia_url}")
    print(f"USPTO      : {uspto_url}  ⚠️ Nhập keyword tay, không hỗ trợ URL param")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        check_trademark(" ".join(sys.argv[1:]))
    else:
        print("Vui lòng nhập keyword. VD: python scripts/check_tm.py barbie")
