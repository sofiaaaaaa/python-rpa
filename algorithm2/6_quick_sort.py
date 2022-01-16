# quick sort 퀵정렬 
# 분할정복(Divide and Conquer) 의 한종류
# pivot(기준점)을 정해서 기준점보다 작은 데이터는 왼쪽, 큰 데이터는 오른쪽으로 모으는 함수를 작성함
# 각 왼쪽과 오른쪽에서는 재귀용법을 사용해서 동일함수를 호출하여 위 작업을 반복한다. 
# 함수는 왼쪽, 기준점, 오른쪽을 리턴한다. 

# 알고리즘 분석
# 병합정렬과 유사하고, 시간복잡도는 O(n log n) 병합정렬보다는 빠르게 정렬된다고 알려짐. 평균적으로는 기준점이 중간에 있다고 예상함. 
# 단 최악의 경우 =>  맨 처음 pivot이 가장 크거나, 가장 작으면 모든 데이터를 비교하는 상황이 나옴 O(n^2)

def qsort(data):
    if len(data) <= 1:
        return data
    
    left, right = list(), list()
    pivot = data[0]

    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])

    return qsort(left) + [pivot] + qsort(right)


import random

data_list = random.sample(range(100), 10)

print(qsort(data_list))

# python list comprehension을 이용해서 간결하게 표현 
def qsort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]

    left = [ item for item in data[1:] if pivot > item ]
    right = [ item for item in data[1:] if pivot <= item ]
    return qsort(left) + [pivot] + qsort(right)