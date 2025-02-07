import requests
import json
import time
from datetime import datetime

def get_real_estate_data(complex_no, page=1):
    cookies = {
        'NAC': 'ZJKPBUQKJE5r',
        'NNB': 'OAHWWQYBGDSGM',
        'nstore_session': '/ia4c1BC77FamzAb3rateo8J',
        'nstore_pagesession': 'i2G1HlqWoNyOclsnyfh-346631',
        'm_loc': 'ddd0726a75d108211a108f4955324bbce9a02c6ed8e3e1fc1e8b20e9b32bb317',
        'NV_WETR_LOCATION_RGN_M': '"MDkyMDA1OTA="',
        'NV_WETR_LAST_ACCESS_RGN_M': '"MDkyMDA1OTA="',
        'tooltipDisplayed': 'true',
        'NFS': '2',
        'NACT': '1',
        'SRT30': '1738389719',
        'SRT5': '1738389719',
        'nhn.realestate.article.rlet_type_cd': 'A01',
        'nhn.realestate.article.trade_type_cd': '""',
        'nhn.realestate.article.ipaddress_city': '1100000000',
        '_fwb': '171MlqbbWUUcWDRgwN5oMrc.1738389721868',
        'landHomeFlashUseYn': 'Y',
        'realestate.beta.lastclick.cortar': '1120000000',
        'REALESTATE': 'Sat%20Feb%2001%202025%2015%3A02%3A25%20GMT%2B0900%20(Korean%20Standard%20Time)',
        'BUC': '9n5lD7HfUveZp-PM7v9tRb-zlkd2Vtr2SPsCs2zcDdE='
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3MzgzODk3NDUsImV4cCI6MTczODQwMDU0NX0.AY-nNR5huRC1TgRObS7zT2-YWCY8Jf_fH7fsA0wGS_g',
        'priority': 'u=1, i',
        'referer': f'https://new.land.naver.com/complexes/{complex_no}?ms=37.555408,127.0369511,17&a=APT&b=A1&e=RETAIL',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
    }

    url = f'https://new.land.naver.com/api/articles/complex/{complex_no}'
    params = {
        'realEstateType': 'APT',
        'tradeType': 'A1',
        'tag': '::::::::',
        'rentPriceMin': '0',
        'rentPriceMax': '900000000',
        'priceMin': '0',
        'priceMax': '900000000',
        'areaMin': '0',
        'areaMax': '900000000',
        'showArticle': 'false',
        'sameAddressGroup': 'false',
        'priceType': 'RETAIL',
        'page': str(page),
        'complexNo': str(complex_no),
        'type': 'list',
        'order': 'rank'
    }

    response = requests.get(url, params=params, cookies=cookies, headers=headers)
    return response.json()

def main():
    complex_no = 2976
    all_articles = []
    
    for page in range(1, 11):
        print(f"{page}페이지 데이터 수집 중...")
        data = get_real_estate_data(complex_no, page)
        articles = data.get('articleList', [])
        
        if not articles:
            print(f"{page-1}페이지까지 수집 완료 (더 이상 데이터가 없습니다)")
            break
        
        all_articles.extend(articles)
        time.sleep(1)
    
    for article in all_articles:
        print(json.dumps(article, ensure_ascii=False, indent=4))
    print(f"총 {len(all_articles)}개의 매물 데이터를 수집했습니다.")

if __name__ == "__main__":
    main()