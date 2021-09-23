# 집합 (set)

my_set = {1,2,3,4, 4, 4}
print(my_set)

my_set2 = {3,4}

#교집합
print(my_set & my_set2)

#합집합
print(my_set | my_set2)
print(my_set.union(my_set2))

#차집합
print(my_set - my_set2)
print(my_set.difference(my_set2))

my_set.add("ccc")

print(my_set)

# 자료구조 변경

menu = {"커피", "우유", "주스"}

print(menu, type(menu))

menu = tuple(menu)

print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

from random import *
users = range(1, 21) # 1부터 20까지 숫자 생성
print(users, type(users))

users = list(users)
print(users, type(users))

print(users)

shuffle(users)

print(users)

