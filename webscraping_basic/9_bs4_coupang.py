import requests 
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}


session = requests.Session()
session.verify = False

res = session.get(url, headers=headers)
res.raise_for_status() # 응답 결과가 오류인 경우 프로그램 종료


soup = BeautifulSoup(res.text, "lxml") # lxml파서를 통해 soup 객체로 만듬 

# print(res.text)


items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

# print(items[0].find("div", attrs={"class": "name"}).get_text())


for item in items:
    # 광고 제품은 제외한다. 
    ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
    if ad_badge:
        print("광고 상품은 제외합니다.")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text() #제품명
    price = item.find("strong", attrs={"class":"price-value"}).get_text() #가격 
    rate = item.find("em", attrs={"class":"rating"}) #평점 
    if rate:
        rate = rate.get_text()
    else:
        print("평점 없는 상품 제외합니다.")
        continue


    # 리뷰 100개 이상, 평점 4.5이상 되는 것만 조회 
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) #평점수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
    else:
        print("평점수 없는 상품 제외합니다.")
        continue

    print(name, price, rate, rate_cnt)
