
# 파이썬 코드 실행 단축 명령어 Fn F5키 


print(not True)
# comment 
# variable
animal = "doggy"
age = 4
print(animal)
print("bbb"+str(age))
print("bbb", "ccc", age)

print(
'''
여러문장 출력하기  
ㅇㅇㅇ
'''
) 

# ㅁㅁㅁ
# ㅠㅠㅠ
# ㅊㅊㅊ
# 여러줄 선택후 control + / 조합키 

print(2**3)

print(5//3)

print(1 != 3)

print(not(1 != 3) and 1 != 3)

print(not(1 != 3) & 1 != 3)

print(not(1 != 3) or 1 != 3)

print(not(1 != 3) | 1 != 3)

print( 5 > 4 > 7 )

number = 2

number /= 2

number *= 2

number %= 2


print(number)

print(abs(-5))

print(pow(4,2)) # 4^2 

print(max(4, 12))

print(min(4, 12))

print(round(3.14))

from math import * 
print(floor(4.90))
print(ceil(3.14))
print(sqrt(3.14))

from random import * 
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성 
print(random() * 10)
print(int(random() * 10))
print(int(random() * 10) + 1)