# 이진탐색 (Binary Search)
# 탐색할 자료를 둘로 나누어 해당 데이터가 있을만한 곳을 탐색하는 방법 
# 순차탐색의 경우 처음부터 하나씩 조사해나가는 방식이지만, 이진탐색은 자료를 반으로 나누어 탐색하므로 데이터가 정렬되어있을 경우 더 빨리 검색할 수 있다. 
# * 분할 정복 알고리즘 (Divide and Conquer)
# * Divide: 문제를 하나 또는 둘 이상으로 나눈다. 
# * Conquer: 나눠진 문제가 충분히 작고, 해결이 가능하다면 해결하고, 그렇지 않다면 다시 나뉜다. 
# * 이진탐색 
# * Divide: 리스트를 두개의 서브 리스트로 나눈다. 
# * Conquer: 검색할 숫자가 중간값보다 크면, 뒷부분의 서브리스트에서 검색할 숫자를 찾고, 반대의 경우는 반대로 처리.

# * 시간복잡도 
# n개의 리스트를 매번 2로 나누어 1이 될 때까지 비교연산을 k회 진행한다. 
# n * 1/2^k = 1 => n = 2^k => log_2_n = log_2_2^k
# log_2_n = k 
# Big O => O(log n)
 
def binary_search(data, search):
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False
    
    medium = len(data) // 2

    if search == data[medium]:
        return True
    else:
        if search > data[medium]:
            return binary_search(data[medium:], search)
        else:
            return binary_search(data[:medium], search)

import random

data_list = random.sample(range(100), 10)

# 1. 리스트를 먼저 오름차순으로 정렬한다.
data_list.sort()

print(binary_search(data_list, 7))


