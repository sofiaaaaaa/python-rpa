# dictionary collection 

cabinet = {3: "bbb", 100: "ccc" }

print(cabinet[3])
print(cabinet.get(3))

# print(cabinet[5]) # 오류로 인한 프로그램 종료 
print(cabinet.get(5, "zzz"))

print(3 in cabinet)

cabinet["c"] = "eee"

print(cabinet)

del cabinet["c"]

print(cabinet)

print(cabinet.items())

cabinet.clear()

print(cabinet)