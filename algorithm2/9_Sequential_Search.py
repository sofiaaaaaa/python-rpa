# 순차탐색 (Sequential Search)
# 탐색은 여러 데이터 중에서 원하는 데이터를 찾아내는 것을 의미한다.
# 데이터가 담겨있는 리스트를 앞에서부터 하나씩 비교해서 원하는 데이터를 찾는 방법 
# * 알고리즘 분석
# 최악의 경우 리스트 길이가 n일 때 n번까지 비교해야함. O(n)

# 랜덤 숫자 배열 만들기 
from random import *
rand_data_list = list()
for num in range(10):
    rand_data_list.append(randint(1,100))

# 배열에서 원하는 데이터의 위치 반환하는 함수 
def sequencial(data_list, search_data):
    for index in range(len(data_list)):
        if data_list[index] == search_data:
            return index
    return -1


