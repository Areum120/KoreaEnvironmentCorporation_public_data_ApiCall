import requests as req
from bs4 import BeautifulSoup as bs
from html_table_parser import parser_functions
#호출한 data 표형식으로 보기
import pandas as pd

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

print(split_4)

# 엑셀 저장
df.to_excel('220408_ev_purchase_subsidy_current_status.xlsx')
print('저장완료')