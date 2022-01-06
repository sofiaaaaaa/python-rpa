import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}


session = requests.Session()
session.verify = False

res = session.get("http://nadocoding.tistory.com", headers=headers)
print("응답코드 ", res.status_code)


res.raise_for_status() # 응답 결과가 오류인 경우 프로그램 종료
print("웹 스크래핑을 진행합니다.")

print(len(res.text))

with open("nadocoing.html", "w", encoding="utf8") as f:
    f.write(res.text)

