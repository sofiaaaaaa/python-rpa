import random
# 버블정렬
# 배열에서 앞에 있는 데이터가 뒤에 있는 데이터보다 크면 서로 바꾸어 배열의 뒤로 이동시키며 정렬하는 방법

# for index in range(데이터의 길이 -1):
#     for index2 in range(데이터의 길이 - index -1):
#         if 앞데이터 > 뒤데이터:
#             만약 끝까지 swap이 일어나지 않으면 break.(정렬이 이미 되어있음 )
#             swap(앞데이터, 뒤데이터)
# * 시간 분석 
# 반복문이 두개이며, 데이터의 길이가 n 
# 최악은 O(n^2) , 최선의 경우는 O(n)


# 테스트데이터 생성
dataList = random.sample(range(100), 50)


def bubblesort(data):
    print("before data : {}".format(data))
    for index in range(len(data)-1):
        swap = False
        for index2 in range(len(data)-index-1):
            print("data[{}]: {}, data[{}]: {}".format(index2, data[index2],  index2+1,  data[index2+1]))
            if data[index2] > data[index2+1]:
                data[index2], data[index2+1] = data[index2+1],data[index2]
                swap = True

        if swap == False:
            break   
    print("after data : {}".format(data))
       

bubblesort(dataList)
            
