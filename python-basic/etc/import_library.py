from math import * 
print(floor(4.90))
print(ceil(3.14))
print(sqrt(3.14))

from random import * 
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성 
print(random() * 10)
print(int(random() * 10))
print(int(random() * 10) + 1)

print(int(random() * 45) + 1)
print(randrange(1, 46)) # 1, 46 미만의 값 생성 

print(randint(1,45)) # 1, 45 이하의 값 생성 

date = randint(4,28)
print(str(date) + "bbb")

sentents3 = """
bbb
ccc
ddd
"""

print(sentents3)

jumin = "831211-1010100"

print("성별 : " + jumin[7])

print("연 :", jumin[0:2])

print("월 : ", jumin[2:4])

print("생년월일 ", jumin[0:6]) 

print("생년월일", jumin[:6]) # 생략가능 
print("생년월일", jumin[7:])

print("생년월일", jumin[-7:]) # 맨 뒤에서 끝까지 
