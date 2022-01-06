import requests 
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"


session = requests.Session()
session.verify = False

res = session.get(url)
res.raise_for_status() # 응답 결과가 오류인 경우 프로그램 종료

soup = BeautifulSoup(res.text, "lxml") # lxml파서를 통해 soup 객체로 만듬 
print(soup.title)
print(soup.title.getText())

print(soup.a) # 처음으로 발견되는 a 태그 보여주기 
print(soup.a.attrs) # 처음으로 발견되는 a 태그의 속성 
print(soup.a['href']) # 처음으로 발견되는 a 태그의 속성 중 href 값


print(soup.find('a', attrs={"class":"Nbtn_upload"}))
print(soup.find(attrs={"class":"Nbtn_upload"}))
print(soup.find('li', attrs={"class":"rank01"}))

rank1 = soup.find('li', attrs={"class":"rank01"})
print(rank1.a.get_text())
print(rank1.next_sibling)
print(rank1.next_sibling.next_sibling)

rank2 = rank1.next_sibling.next_sibling
print(rank2.a.getText())

rank3 = rank2.next_sibling.next_sibling

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.getText())

print(rank1.paren)

rank1.find_next_sibling()

rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())

rank1.find_next_siblings("li")

webtoon = soup.find("a", text="독립일기-시즌2 36화 나의 20대 (1)")
print(webtoon)