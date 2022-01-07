import requests 
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"


session = requests.Session()
session.verify = False

res = session.get(url)
res.raise_for_status() # 응답 결과가 오류인 경우 프로그램 종료


soup = BeautifulSoup(res.text, "lxml") # lxml파서를 통해 soup 객체로 만듬 

# 만화정보와 링크 가져오기 
cartoons = soup.find_all("td", attrs={"class", "title"})
title = cartoons[0].a.get_text()

print(title)

link = cartoons[0].a["href"]

print(title)
print("https://comic.naver.com"+link)

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com"+cartoon.a["href"]
    print(title, link)


# 평점구하기 
total_rates = 0
cartoons = soup.find_all("div", attrs={"class", "rating_type"})
for catoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)

print("전체점수: "+ total_rates)
print("평균점수: "+ total_rates / len(cartoons))


