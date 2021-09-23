absent = [2,5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("{0}.. end".format(student))
        break
    print("{0} zzz".format(student))


students = [1,2,3,4,5]
print(students)

students = [i+100 for i in students]

print(students)

students = ["aaa", "bbb", "ccc"]
#students = [len(i) for i in students]
#print(students)

students = [i.upper() for i in students]
print(students)

from random import * 
cnt = 0 
for i in range(1,51): 
    time = randrange(5,51) 
    if 5 <= time <= 15:
        print("[0] {0} zzzzz {1}".format(i, time))
        cnt += 1
    else: 
        print("[ ] {0} zzzzz {1}".format(i, time))

print("total : {0}".format(cnt))