# 재귀함수 

def factorial(num):
    if num <= 1:
        return num
    return num * factorial(num -1)

for num in range(10):
    print(factorial(num))

# 스택이 재귀호출의 전형적인 예
# 함수는 내부적으로 스택처럼 관리된다. 계속 함수호출을 쌓다가 더이상 호출할 함수가 없으면, 마지막에 호출한 함수부터 실행하기 시작한다. 

# 1부터 num까지 곱 출력하기 두가지 방법 
def multiple(num):
    return_value = 1
    for index in range(1, num +1):
        return_value = return_value * index
    return return_value

def multiple(num):
    if num <= 1:
        return num
    return num * multiple(num -1)


# 숫자가 들어있는 리스트의 합을 구하는 함수 
def sum_list(data):
    if len(data) == 1:
        return data[0]
    return data[0] + sum_list(data[1:])

import random
data = random.sample(range(100), 10)
print(sum_list(data))

# 리스트 슬라이싱 
string = "abcd"
print(string[-1]) # e
print(string[0]) # D
print(string[1:-1]) # av
print(string[:-1]) # Dav

# 회문 (pailndrome) : 순서를 거꾸로 읽어도 똑같은 단어와 문장 
def palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False


# 정수 n을 입력받아,  n이 홀수면 3 * n +1, n이 짝수면 n을 2로 나눈다. 이렇게 계속 진행해서 n이 1이 되는 과정을 모두 출력하는 함수 
def func(n):
    print(n)
    if n == 1:
        return n 
    
    if n % 2 == 1: # 홀수
        return (func(3*n)+1)
    else:
        return (func(int(n/2)))

# 정수 n을 1,2,3의 합으로 나타낼 수 있는 방법의 수를 구하는 함수 
def func(data):
      if data == 1:
          return 1
      elif data == 2:
          return 2
      elif data == 3:
          return 4   

      return func(data -1) + func(data -2) + func(data -3)
