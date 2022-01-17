import requests 
import re
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.bithumb.com/trade/order/BTC_KRW"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

# 빗썸 코인명 / 코인 약어 리스트 출력 
session = requests.Session()
session.verify = False

res = session.get(url, headers=headers)
res.raise_for_status() # 응답 결과가 오류인 경우 프로그램 종료


soup = BeautifulSoup(res.text, "lxml") # lxml파서를 통해 soup 객체로 만듬 

# print(res.text)

items = soup.find_all("a", attrs={"class":re.compile("GA_PUBLIC_COIN_LIST")})

# print(items[0].find("div", attrs={"class": "tx_l tx_link"}).getText())
print("{")
for item in items:
    divText = item.find("div", attrs={"class":"tx_l tx_link"})
    divText = str(divText)
    divText = divText.replace('<div class="tx_l tx_link">', "")
    divTextArr = divText.split("<")
    if len(divTextArr) > 1:
        coinNameKr = divTextArr[0]
        # print(coinNameKr)
        spanText = item.find("span", attrs={"class":"coinSymbol sort_coin"}).get_text()
        acronymsArr = spanText.split("/")
        if acronymsArr[1] == "KRW" : 
            # print(acronymsArr[0])
            coinAcronyms = acronymsArr[0]
            print('"{}":"{}",'.format(coinAcronyms, coinNameKr))

print("}")
