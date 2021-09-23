weather = input("오늘날씨?비")
if weather == "비": 
    print("비")
elif weather == "미세먼지":
    print("mm")
else: 
    print("xxx")

temp = int(input("how temperate???"))
if 40 <= temp:
    print("hhh")
elif 0 <= temp < 10:
    print("mm")
else: 
    print("ccc")