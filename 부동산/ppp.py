import pprint;
import json;
import requests;
import xmltodict;
import pandas as pd;
import os
import sys
import openpyxl

code = ()

wb = openpyxl.load_workbook('./데이터.xlsx')
sheet1 = wb.active

def call_data(areacode,tradeday):

    queryParams = '?'+'serviceKey=niFwXD2Gk0Mc8ZJYQUt10m4OAtfcdKa2EoYxsMDG6D0n7ooX5IbGCXuzNBBBQIX31wdSW8as4AC95qTMMSlvlQ=='+ '&pageNo=' + '1' + '&numOfRows=' + '9999' + '&LAWD_CD=' + str(areacode) + '&DEAL_YMD=' + str(tradeday)

    key = "niFwXD2Gk0Mc8ZJYQUt10m4OAtfcdKa2EoYxsMDG6D0n7ooX5IbGCXuzNBBBQIX31wdSW8as4AC95qTMMSlvlQ=="
    url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev"

#http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey=niFwXD2Gk0Mc8ZJYQUt10m4OAtfcdKa2EoYxsMDG6D0n7ooX5IbGCXuzNBBBQIX31wdSW8as4AC95qTMMSlvlQ%3D%3D&pageNo=1&numOfRows=10&LAWD_CD=11110&DEAL_YMD=201512

    response = requests.get(url+queryParams).content.decode('utf-8')
    dict = xmltodict.parse(response)

    try:

        jsonString = json.dumps(dict['response']['body'], ensure_ascii=False)
        jsonObj = json.loads(jsonString)

        df = pd.read_json(json.dumps(jsonObj['items']['item']))
        print(type(jsonObj['items']['item']))
        return jsonObj['items']['item']

    except:
        print("[%s] None Data!" %areacode)
        return True;


example = call_data(11110, 201401)

print(example)

sheet1.append(example)
wb.save('데이터.xlsx')



