import requests

res = requests.get("http://naver.com")
print("응답코드 ", res.status_code)

# if res.status_code == requests.codes.ok:
#     print("정상")
# else: 
#     print("에러!! ")

res.raise_for_status() # 응답 결과가 오류인 경우 프로그램 종료
print("웹 스크래핑을 진행합니다.")

print(len(res.text))

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)

