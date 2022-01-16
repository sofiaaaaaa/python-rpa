# 동적계획법(Dynamic Programming)과 분할정복(Divide and Conquer)

# 동적계획법 : 입력크기가 작은 부분 문제들을 해결한 후, 해당 부분 문제의 해를 활용해서, 보다 큰 크기의 부분 문제를 해결하고, 최종적으로 전체 문제를 해결하는 알고리즘
# 상향식 접근법. 가장 최하위 해답을 구한후 이를 저장하고 해당 결과값을 이용해서 상위 문제를 풀어감
# Memoization 기법 : 프로그램 실행시 이전에 계산한 값을 저장하여, 다시 계산하지 않도록 전체 실행속도를 빠르게 하는 기술. 
# 문제를 잘게 쪼갤때 부분 문제는 중복되어 재활용된다. 
# 피보나치 수열 
# n = 0 => 0
# n = 1 => 1
# n > 1 => F(n-1) + F(n-2)


# 분할 정복
# 문제를 나눌 수 없을 때까지 나누어서 각각을 풀면서 다시 합병하여 문제의 답을 얻는 알고리즘
# 하향식 접근법으로 상위의 해답을 구하기 위해서 아래로 내려가기 위해 하위의 해답을 구하는 방식
# 일반적으로 재귀함수로 구현함..
# 문제를 잘게 쪼갤때 부분 문제는 서로 중복되지 않는다. 
# 병합 정렬, 퀵 정렬

# 공통점 : 문제를 잘게 쪼개서, 가장 작은 단위로 분할 
# 차이점 : 
# * 동적계획법: 부분 문제는 중복되어, 상위 문제 해결시 재활용됨, Memoization (부분 문제의 해답을 저장해서 재활용하는 최적화 기법으로 사용)
# * 분할정복법: 부분 문제는 서로 중복되지 않음. Memoization사용안함 


# recusive를 활용한 피보나치수열 계산 함수 
def fibo(num):
    if num <= 1: 
        return num 
    
    return fibo(num-1) + fibo(num-2)

print(fibo(4))


# fibo(4) = fibo(3) + fibo(2)
# fibo(3) = fibo(2) + fibo(1)
# fibo(2) = fibo(1) + fibo(0) 
# fibo(2), fibo(1) 이 몇차례 스택에 쌓여서 중복되어 실행되는 문제가 발생함. 


# 동적 계획법 활용. (Memoization 기법추가)
# fun-coding.org 사이트의 python Comprehension 참조  
# pythontutor.com/live.html#mode=edit 에서 실행과정 확인 
def fibo_dp(num):
    # 빈 배열에 0으로 채워서 넣기, 마지막 요소에는 피보나치수열 계산한 최종값이 저장된다. 
    # n이 배열의 index값과 동일해야하기 때문에 배열의 길이를 n에 1을 더한 값이어야한다. 
    # Memoization : 캐시 배열 생성 
    cache = [ 0 for index in range(num + 1)]
    cache[0] = 0 # n = 0, 1 일 때는 0, 1을 출력하기 때문.
    cache[1] = 1

    # 배열 index=2부터 시작하여, 배열의 0번째, 1번째 요소에 이미 저장된 값을 이용해서 값을 더해 저장한다.
    for index in range(2, num + 1):
        cache[index] = cache[index -1] + cache[index -2]
        return cache[num]

