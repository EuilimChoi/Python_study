# 1-1. 데이터 가져오기
import requests
import datetime
import xml.etree.ElementTree as ET
import pandas as pd;
import os


url ="http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?"
service_key = "niFwXD2Gk0Mc8ZJYQUt10m4OAtfcdKa2EoYxsMDG6D0n7ooX5IbGCXuzNBBBQIX31wdSW8as4AC95qTMMSlvlQ=="
base_date = "202101" 
gu_code = '11110' ## 법정동 코드 5자리라면, 구 단위로 데이터를 확보하는 것. 11215 = 광진구

payload = "LAWD_CD=" + gu_code + "&" + \
          "DEAL_YMD=" + base_date + "&" + \
          "serviceKey=" + service_key + "&" 
          
res = requests.get(url + payload)


def get_items(response):
    root = ET.fromstring(response.content)
    item_list = []
    for child in root.find('body').find('items'):
        elements = child.findall('*')
        data = {}
        for element in elements:
            tag = element.tag.strip()
            text = element.text.strip()
            # print tag, text
            data[tag] = text
        item_list.append(data)  
    return item_list
    
items_list = get_items(res)
items = pd.DataFrame(items_list) 
items.head()

code_file = './법정동코드 전체자료.txt'
code = pd.read_csv('./법정동코드 전체자료.txt', encoding='cp949', sep='\t')


code.columns = ['code', 'name', 'is_exist']
code = code [code['is_exist'] == '존재']
code['code'] = code['code'].apply(str) 


year = [str("%02d" %(y)) for y in range(2015, 2021)]
month = [str("%02d" %(m)) for m in range(1, 13)]
base_date_list = ["%s%s" %(y, m) for y in year for m in month ]


gu = "강남구"
gu_code = code[ (code['name'].str.contains(gu) )]
gu_code = gu_code['code'].reset_index(drop=True)
gu_code = str(gu_code[0])[0:5]
print(gu_code)

def get_data(gu_code, base_date):
    url ="http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?"
    service_key = "niFwXD2Gk0Mc8ZJYQUt10m4OAtfcdKa2EoYxsMDG6D0n7ooX5IbGCXuzNBBBQIX31wdSW8as4AC95qTMMSlvlQ=="

    payload = "&pageNo=" + '1' + "&"+\
            "&numOfRows=" + '9999'+ "&"+\
            "LAWD_CD=" + gu_code + "&" + \
            "DEAL_YMD=" + base_date + "&" + \
            "serviceKey=" + service_key \

    res = requests.get(url + payload)
        
    return res

items_list = []
for base_date in base_date_list:
    res = get_data(gu_code, base_date)
    items_list += get_items(res)
    
len(items_list)

items = pd.DataFrame(items_list) 
items.head()
items.to_excel(os.path.join("%s_%s~%s.xlsx" %(gu, year[0], year[-1])), index=False,encoding="euc-kr") 