print("aaa", "bbb", sep=",") # sep - 구분자 지정 

print("aaa", "bbb", "ccc", sep=",", end="?") # end - 줄바꿈 외에 다른 문자로 변경 가능함 
print("zzz")

import sys
print("ccc", "ddd", file=sys.stdout) # 표준 출력 
print("ccc", "ddd", file=sys.stderr) # 표준 에러 

# dictionary
scores = {"수학": 100, "영어": 98}

for subject, score in scores.items():
    #print("{0}, {1}".format(subject, score))
    print(subject.ljust(8), str(score).rjust(4), sep=":") # 총8글자공간 확보후 왼쪽 정렬 후 줄맞춤 

for num in range(1, 21):
    print("대기번호 : "+ str(num).zfill(3)) # 3자리 공간을 확보하고 나머지는 0으로 채우기 

answer = input("aaaa : ")

print(answer)   