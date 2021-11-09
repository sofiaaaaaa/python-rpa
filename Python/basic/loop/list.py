# 리스트 []

subway = [10, 20, 30]
print(subway)

print(subway.index(10))

subway.append(40)

print(subway)

subway.insert(1, 156)
print(subway)
print(subway.pop())
print(subway)

subway.append(10)

print(subway)

print(subway.count(10))


num_list = [5,1,25,2,4,6]

print(num_list.sort())

print(num_list)

num_list.reverse()

print(num_list)


num_list.clear()

print(num_list)

#다양한 자료형 함께 사용 가능하다. 
mix_list = ["aaa", 10, True]

print(mix_list)

num_list.extend(mix_list)

print(num_list)