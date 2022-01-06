import requests 
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"


session = requests.Session()
session.verify = False

res = session.get(url)
res.raise_for_status() # 응답 결과가 오류인 경우 프로그램 종료

soup = BeautifulSoup(res.text, "lxml") # lxml파서를 통해 soup 객체로 만듬 