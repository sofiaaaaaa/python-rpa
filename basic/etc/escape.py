# escape 문자 

print("bbbb \n ccc")
print("""
    "aaa" bbbb
"""
)

print('"bbb" ccc')
print("aaa ccc \"ccc\" ")

# \\ : 문장내에서 하나의 역슬러시.. 
print("\\c")

# \r : 커서를 앞으로 이동 
print("red aaa \rPine") # Pineaaa

# \b : 백스페이스 (한 글자 삭제)
print("Red\bApple")

# \t: 탭 
print("Red\tApple")


url = "http://naver.com"

my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e"))

print("{0}'s password is {1}.".format(url, password))
