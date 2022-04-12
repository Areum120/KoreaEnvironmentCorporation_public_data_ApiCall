# -*- coding: utf-8 -*-
# 한글 인코딩 에러
import requests as req
from bs4 import BeautifulSoup as bs
from html_table_parser import parser_functions#호출한 data 표형식으로 보기
import pandas as pd
import datetime


url = 'https://ev.or.kr/portal/localInfo'

req = req.get(url)
soup = bs(req.text, 'html.parser')
data = soup.find('table', {'class':'table_02_2_1'})
# print(data)

# table 갖고 오기
table = parser_functions.make2d(data)
# print(table[1:])
# print(table[0])

# 모든 열 출력
pd.set_option('display.max_columns', None)

# 데이터프레임
df = pd.DataFrame(data=table[2:], columns=table[0])
# print(df)

# 민간공고대수 칼럼 parsing
split_1 = df.민간공고대수.str.split(' ')

# series->dataframe
split_1= split_1.apply(lambda x:pd.Series(x))

# 컬럼명지정
split_1.columns = ['민간공고대수_전체', '민간공고대수_우선순위', '민간공고대수_법인기관', '민간공고대수_택시', '민간공고대수_우선비대상']

# 괄호값 제거(정규식 특수문자 제거)
split_1['민간공고대수_우선순위'] = split_1['민간공고대수_우선순위'].str.replace(pat=r'[^\w]', repl=r'', regex=True)
split_1['민간공고대수_법인기관'] = split_1['민간공고대수_법인기관'].str.replace(pat=r'[^\w]', repl=r'', regex=True)
split_1['민간공고대수_택시'] = split_1['민간공고대수_택시'].str.replace(pat=r'[^\w]', repl=r'', regex=True)
split_1['민간공고대수_우선비대상'] = split_1['민간공고대수_우선비대상'].str.replace(pat=r'[^\w]', repl=r'', regex=True)

# print(split_1)

# 접수대수 칼럼 parsing
split_2 = df.접수대수.str.split(' ')

# series->dataframe
split_2= split_2.apply(lambda x:pd.Series(x))

# 컬럼명지정
split_2.columns = ['접수대수_우선순위', '접수대수_법인기관', '접수대수_택시', '접수대수_우선비대상']

# 괄호값 제거(정규식 특수문자 제거)
split_2['접수대수_우선순위'] = split_2['접수대수_우선순위'].str.replace(pat=r'[^\w]', repl=r'', regex=True)
split_2['접수대수_법인기관'] = split_2['접수대수_법인기관'].str.replace(pat=r'[^\w]', repl=r'', regex=True)
split_2['접수대수_택시'] = split_2['접수대수_택시'].str.replace(pat=r'[^\w]', repl=r'', regex=True)
split_2['접수대수_우선비대상'] = split_2['접수대수_우선비대상'].str.replace(pat=r'[^\w]', repl=r'', regex=True)

# print(split_2)

# 출고대수 칼럼 parsing
split_3 = df.출고대수.str.split(' ')

# series->dataframe
split_3= split_3.apply(lambda x:pd.Series(x))

# 컬럼명지정
split_3.columns = ['출고대수_전체', '출고대수_우선순위', '출고대수_법인기관', '출고대수_택시', '출고대수_우선비대상']

# 괄호값 제거(정규식 특수문자 제거)
split_3['출고대수_우선순위'] = split_3['출고대수_우선순위'].str.replace(pat=r'[^\w]', repl=r'', regex=True)
split_3['출고대수_법인기관'] = split_3['출고대수_법인기관'].str.replace(pat=r'[^\w]', repl=r'', regex=True)
split_3['출고대수_택시'] = split_3['출고대수_택시'].str.replace(pat=r'[^\w]', repl=r'', regex=True)
split_3['출고대수_우선비대상'] = split_3['출고대수_우선비대상'].str.replace(pat=r'[^\w]', repl=r'', regex=True)

# print(split_3)

# 출고잔여대수 칼럼 parsing
split_4= df.출고잔여대수.str.split(' ')

# series->dataframe
split_4= split_4.apply(lambda x:pd.Series(x))

# 컬럼명지정
split_4.columns = ['출고잔여대수_전체', '출고잔여대수_우선순위', '출고잔여대수_법인기관', '출고잔여대수_택시', '출고잔여대수_우선비대상']

# 괄호값 제거(정규식 특수문자 제거)
split_4['출고잔여대수_우선순위'] = split_4['출고잔여대수_우선순위'].str.replace(pat=r'[^\w]', repl=r'', regex=True)
split_4['출고잔여대수_법인기관'] = split_4['출고잔여대수_법인기관'].str.replace(pat=r'[^\w]', repl=r'', regex=True)
split_4['출고잔여대수_택시'] = split_4['출고잔여대수_택시'].str.replace(pat=r'[^\w]', repl=r'', regex=True)
split_4['출고잔여대수_우선비대상'] = split_4['출고잔여대수_우선비대상'].str.replace(pat=r'[^\w]', repl=r'', regex=True)

# print(split_4)

# 필요 데이터만 merge(date, sido, region, split_1, split_2, split_3, split_4, note)

# 일자 생성
now = datetime.datetime.now()  # 지금시간
nowToday = now.strftime('%Y%m%d')  # 일자
# print(nowToday)

# print(type(split_1))


# merge
result = pd.concat([split_1, split_2, split_3, split_4], axis=1)
# print(result)


# # date칼럼 생성
result['date'] = nowToday
result['sido'] = df['시도']
result['region'] = df['지역구분']
result['note'] = df['비고']

# 순서변경
result = result[['date', 'sido', 'region', '민간공고대수_전체', '민간공고대수_우선순위', '민간공고대수_법인기관', '민간공고대수_택시', '민간공고대수_우선비대상', '접수대수_우선순위', '접수대수_법인기관', '접수대수_택시', '접수대수_우선비대상', '출고대수_전체', '출고대수_우선순위', '출고대수_법인기관', '출고대수_택시', '출고대수_우선비대상', '출고잔여대수_전체', '출고잔여대수_우선순위', '출고잔여대수_법인기관', '출고잔여대수_택시', '출고잔여대수_우선비대상']]

# 이름변경
result.columns = ['date', 'sido', 'region', 'num_notice_all', 'num_notice_priority','num_notice_corp','num_notice_taxi','num_notice_normal', 'num_recept_priority', 'num_recept_corp', 'num_recept_taxi','num_recept_normal','num_release_all','num_release_priority','num_release_corp','num_release_taxi', 'num_release_normal', 'num_remains_all', 'num_remains_priority','num_remains_corp','num_remains_taxi','num_remains_normal']
print(result)


# 엑셀 저장
result.to_excel(f'{nowToday}_ev_purchase_subsidy_current_status.xlsx')
print('저장완료')