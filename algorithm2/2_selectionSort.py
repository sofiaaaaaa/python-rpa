# 선택정렬 selection sort 
# 다음과 같은 순서를 반복하며 정렬하는 알고리즘 
# 1. 주어진 데이터중에서 최소값을 찾는다.
# 2. 해당 최소값을 데이터 맨 앞에 위치한 값과 교체한다.
# 3. 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복한다. 

# for stand in range(데이터길이 -1):
#   lowest = stand
#   for index in range(stand +1, len(data)):
#       if data[lowest] > data[index]:
            # lowest = index
    # swap (lowest, index)

def selection_sort(data):
    for stand in range(len(data) -1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return data

import random

# 100개의 데이터 중에서 10개만 랜덤으로 뽑아 리스트로 만든다. 
data_list = random.sample(range(100), 10)

print(selection_sort(data_list))

    
# 알고리즘 분석 
# 반복문이 두개이며, 데이터의 길이가 n 
# 최악은 O(n^2) 정확하게는 (n*(n-1))/2  , 최선의 경우는 O(n)