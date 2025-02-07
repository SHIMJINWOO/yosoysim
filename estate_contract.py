import requests
import xml.etree.ElementTree as ET

def fetch_apartment_data(lawd_cd: str, deal_ymd: str):
    url = "http://apis.data.go.kr/1613000/RTMSDataSvcAptTrade/getRTMSDataSvcAptTrade"
    params = {
        "LAWD_CD": lawd_cd,
        "DEAL_YMD": deal_ymd,
        "serviceKey": "zHCj2Vd7CDTEdo2+vSqSIs/EOoUc91Fvbwi6sF0DUCv0clSjJTOxThCG1PyeODyeAqGWcULR71ivfcUa6H77KA=="
    }
    
    response = requests.get(url, params=params)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text (First 500 chars): {response.text[:5000]}")  # XML 일부 출력 확인
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def parse_apartment_data(xml_data):
    root = ET.fromstring(xml_data)
    items = []
    
    for item in root.findall(".//item"):
        data = {
            "거래금액": item.find("dealAmount").text.strip() if item.find("dealAmount") is not None else "N/A",
            "건축년도": item.find("buildYear").text if item.find("buildYear") is not None else "N/A",
            "년": item.find("dealYear").text if item.find("dealYear") is not None else "N/A",
            "월": item.find("dealMonth").text if item.find("dealMonth") is not None else "N/A",
            "일": item.find("dealDay").text if item.find("dealDay") is not None else "N/A",
            "법정동": item.find("umdNm").text.strip() if item.find("umdNm") is not None else "N/A",
            "아파트": item.find("aptNm").text.strip() if item.find("aptNm") is not None else "N/A",
            "전용면적": item.find("excluUseAr").text if item.find("excluUseAr") is not None else "N/A",
            "층": item.find("floor").text if item.find("floor") is not None else "N/A"
        }
        items.append(data)
    
    return items

if __name__ == "__main__":
    lawd_cd = "11110"  # 서울 종로구
    deal_ymd = "202012"  # 2020년 12월
    
    xml_data = fetch_apartment_data(lawd_cd, deal_ymd)
    
"""     if xml_data:
        data_list = parse_apartment_data(xml_data)
        for data in data_list[:5]:  # 상위 5개만 출력
            print(data)
 """