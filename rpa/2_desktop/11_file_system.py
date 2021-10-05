import os

# print(os.getcwd()) # 현재 작업공간 

# # 현재 디렉토리 변경하기 
# os.chdir("rpa")

# print(os.getcwd()) 

# # 부모폴더로 이동 
# os.chdir("..")
# print(os.getcwd())

# os.chdir("../..")
# print(os.getcwd())

# # 절대 경로 
# os.chdir("C:/")
# print(os.getcwd()) 

# 파일 경로 만들기 
# file_path = os.path.join((os.getcwd(), "my_file.txt"))
# print(os.getcwd()) 

# 파일 경로에서 폴더 정보 가져오기 "r" 입력하면 역슬래시 없이 인식가능 
print(os.path.dirname(r"C:\Users\X0126516\Documents\python\python-rpa\README.md"))

# # 파일 정보 가져오기 
# import time
# import datetime

# # 파일의 생성일자 
# ctime = os.path.getctime(".gitignore")
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime))
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정일자 
# mtime = os.path.getmtime(".gitignore")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 접근날짜 
# atime = os.path.getatime(".gitignore")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# # 파일 크기 byte단위  
# size = os.path.getsize(".gitignore")
# print(size)

# 파일목록가져오기 

# print(os.listdir()) #모든폴더 파일 가져오기
# print(os.listdir("basic")) #특정폴더 하위 폴더, 파일목록

# result = os.walk("basic") #주어진 폴더 밑 모든 폴더, 파일
# # print(result)
# #3개의 값을 가진 튜플 반환
# for root, dirs, files in result:
#     print(root, dirs, files)

# result = os.walk(".") # 현재폴더 

# 폴더내에 특정 파일 찾기 
# name = "11_file_system.py"
# result = []
# for root, dir, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root, name)) # 경로 반환 

# print(result)

# 특정 확장자 파일 찾기 
import fnmatch
pattern = "*.py" #  .py로 끝나는 모든 파일 
result = []
for root, dir, files in os.walk("."):
    for name in files: 
        if fnmatch.fnmatch(name, pattern):
            result.append(os.path.join(root, name))

print(result)
            