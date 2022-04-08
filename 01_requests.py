
import requests
import json
import pandas as pd
import openpyxl

# 공공데이터 API Call (한국환경공단 전기차 구매 보조금 data)
key='CTFUEzKcx7CIIBqAvwD%2BJ9MObIpZoglK5TtrmnaBqeaiaFS%2FDlPS2Bt%2Fq52xl%2B33kK8hAHvCMK1b7Mu77hN17w%3D%3D'
page = '1'
limit = '169'
url=f'https://api.odcloud.kr/api/15039172/v1/uddi:30352622-49f8-4856-8bcd-c671c10cc251_201909191317?page={page}&perPage={limit}&serviceKey={key}'
#parameter 서버로 넘겨주는 정보
print(url)

# 데이터불러오기
r= requests.get(url).content#json파일에 접근

jo = json.loads(r)
item = jo['data']

# print(len(item))#169개

# 모든 열 출력
pd.set_option('display.max_columns', None)

# 데이터프레임으로 변환
df = pd.DataFrame.from_dict(item, orient='columns')
print(df)

# 엑셀 저장
df.to_excel('ev_purchase_subsidy.xlsx')