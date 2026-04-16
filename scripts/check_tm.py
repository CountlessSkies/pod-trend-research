import sys

def check_trademark(keyword):
    """
    Placeholder cho script kiểm tra Trademark tự động.
    Hiện tại sẽ trả về link tra cứu nhanh cho Assistant.
    """
    safe_kw = keyword.replace(' ', '+')
    trademarkia_url = f"https://www.trademarkia.com/trademarks-search.aspx?tn={safe_kw}"
    uspto_url = f"https://tmsearch.uspto.gov/search/search-results" # URL gốc của TESS
    
    print(f"Keyword: {keyword}")
    print(f"Check here: {trademarkia_url}")
    return trademarkia_url

if __name__ == "__main__":
    if len(sys.argv) > 1:
        check_trademark(" ".join(sys.argv[1:]))
    else:
        print("Vui lòng nhập keyword.")
