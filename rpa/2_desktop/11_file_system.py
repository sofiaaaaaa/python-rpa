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

# 파일 정보 가져오기 
import time
import datetime

# 파일의 생성일자 
ctime = os.path.getctime(".gitignore")
print(ctime)
print(datetime.datetime.fromtimestamp(ctime))
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 수정일자 
mtime = os.path.getmtime(".gitignore")
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 접근날짜 
atime = os.path.getatime(".gitignore")
print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 파일 크기 byte단위  
size = os.path.getsize(".gitignore")
print(size)
