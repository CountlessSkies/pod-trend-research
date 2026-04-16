import sys

def check_trademark(keyword):
    """
    Trả về link tra cứu Trademark nhanh cho AI/người dùng mở thủ công.

    Tạm bỏ USPTO vì Trademarkia đã đủ và USPTO SPA không hỗ trợ URL param.
    """
    safe_kw = keyword.replace(' ', '+')
    trademarkia_url = f"https://www.trademarkia.com/trademarks-search.aspx?tn={safe_kw}"
    # uspto_url = "https://tmsearch.uspto.gov/"  # SPA, không hỗ trợ URL param — bỏ qua tạm thời

    print(f"Keyword    : {keyword}")
    print(f"Trademarkia: {trademarkia_url}")
    # print(f"USPTO      : {uspto_url}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        check_trademark(" ".join(sys.argv[1:]))
    else:
        print("Vui lòng nhập keyword. VD: python scripts/check_tm.py barbie")
