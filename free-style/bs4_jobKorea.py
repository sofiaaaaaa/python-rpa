import requests 
import re
from bs4 import BeautifulSoup

# SI프로젝트 구인 광고인지 확인 
def checkSiProject(str):
    keywords = ["JAVA", "VUEJS", "SI", "프리랜서", "프로젝트", "개월", "고급", "중급", "개발"]
    for keyword in keywords:
        if str.upper().find(keyword) == -1:
            return False
        return True

# 잡코리아 검색 API 호출 
def callSearchProjects(pageNo):
    # SI 프리랜서 JAVA 검색 
    url = "https://www.jobkorea.co.kr/Search/?stext=SI%20%ED%94%84%EB%A6%AC%EB%9E%9C%EC%84%9C%20JAVA&Page_No={}".format(pageNo)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    session = requests.Session()
    session.verify = False
    res = session.get(url, headers=headers)
    res.raise_for_status() # 응답 결과가 오류인 경우 프로그램 종료
    soup = BeautifulSoup(res.text, "lxml") # lxml파서를 통해 soup 객체로 만듬 
    items = soup.find_all("li", attrs={"class":re.compile("^list-post")})
    return items

pageNo = 1
while True:
    items = callSearchProjects(pageNo)
    if items == None or pageNo > 2:
        break
    
    pageNo += 1
    for item in items:
        
        companyName = item.find("a", attrs={"class":"name"})
        if companyName:
            print(companyName)
            print(companyName["href"])
            companyName = companyName.get_text()
        
        title = item.find("a", attrs={"class":"title"})
        if title:
            title = title.get_text()
            title = title.strip()

        option = item.find("p", attrs={"class":"option"})
        if option:
            option = option.get_text()

        tags = item.find("p", attrs={"class":"etc"})
        if tags:
            tags = tags.get_text()
        
        option = option.strip()
        option = option.replace("\n", ", ")
        # option = option.replace("\n", "::")
        # options = option.split("::")
        # print(options) # 5개 또는 6개 

        if checkSiProject(title) or checkSiProject(tags):
            print("* 회사명 : {}".format(companyName))
            print("* 제목 : {}".format(title))
            if option: print("* 조건 : {}".format(option))
            if tags: print("* 키워드 : {}".format(tags))
            print()
            print()
