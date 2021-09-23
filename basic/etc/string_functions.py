python = "Python is Amazing Python"
print(python.lower())

print(python.upper())

print(python[0].isupper())

print(len(python))

print(python.replace("Python", "Java"))

index = python.index("n")

print(index)

print(python.index("n", index + 1))

print(python.find("n"))
print(python.find("JAVA")) # 없으면 -1 반환 


print(python.index("Java")) # index 함수는 리턴값이 없으면 프로그램 에러가 발생함 
