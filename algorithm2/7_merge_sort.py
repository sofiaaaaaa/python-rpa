# 병합정렬 (merge sort) - 합병 정렬 
# 재귀용법을 활용한 정렬알고리즘 
# 1. 리스트를 절반으로 잘라 비슷한 크기의 두개의 리스트로 나눈다.
# 2. 각 부분 리스트를 재귀적으로 합병정렬을 이용해서 정렬한다. 
# 3. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다. 

# 데이터리스트를 앞뒤로 자르는 코드
# def split(data):
#     medium = int(len(data) / 2)
#     left = data[:medium] # medium이 length로 인식됨 
#     right = data[medium:]

# data_list = [1,3,12,4,2]

# 알고리즘 분석 
# * 시간복잡도 : 
# 각 단계는 O(n)
# 두개의 리스트로 쪼개지는데 각 단계별로 항상 log_2_n 만큼 만들어진다. 시간 복잡도는 O(logn). 여기서 2는 상수여서 삭제됨 
# 단계별 시간복잡도는 O(n) * O(log n) = O(n logn)


def merge(left, right):
    merged = []
    left_point, right_point = 0, 0
    print(left, right)
    # case1: left/right 아직 남아있을 때
    while(len(left) > left_point and len(right) > right_point):
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2: left만 남아있을 때
    while(len(left) > left_point):
        merged.append(left[left_point])
        left_point += 1

    # case3: right만 남아있을 때
    while(len(right) > right_point):
        merged.append(right[right_point])
        right_point += 1
    
    return merged

def mergesplit(data):
    if len(data) <= 1:
        return data

    medium = int(len(data) /2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)


import random
data_list = random.sample(range(100), 10)
mergesplit(data_list)
