# 삽입정렬 insertion sort
# 배열의 두번째 인덱스부터 시작하며, 이전 값이 큰 경우 다음 값과 바꾸어간다. 

# for index in range(데이터길이 -1):
#     for index2 in range(index +1, 1, -1): 순서가 뒤 => 앞 으로 거꾸로 진행됨
#         if 앞데이터 data[index2] > 뒤의 데이터 data[index2 -1]:
#              swap()
#         else:
#               break 



for index in range(10, 1, -1):
    print(index)



def insertion_sort(data):
    for index in range(len(data)-1):
        for index2 in range(index +1, 0, -1):
            if data[index2] < data[index2-1]:
                data[index2], data[index2-1] = data[index2-1], data[index2]
            else:
                break
    return data


import random

# 100개의 데이터 중에서 10개만 랜덤으로 뽑아 리스트로 만든다. 
data_list = random.sample(range(100), 10)
print(data_list)
print(insertion_sort(data_list))


# 알고리즘 분석 
# 반복문이 두개이며, 데이터의 길이가 n 
# 최악은 O(n^2) 정확하게는 (n*(n-1))/2  , 최선의 경우는 O(n)