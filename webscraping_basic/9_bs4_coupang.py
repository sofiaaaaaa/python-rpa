import requests 
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?component=&q=%EA%B3%A8%EB%93%9C%EB%B0%95%EC%8A%A4&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}


session = requests.Session()
session.verify = False

res = session.get(url, headers=headers)
res.raise_for_status() # 응답 결과가 오류인 경우 프로그램 종료


soup = BeautifulSoup(res.text, "lxml") # lxml파서를 통해 soup 객체로 만듬 

# print(res.text)


items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

print(items[0].find("div", attrs={"class": "name"}).get_text())