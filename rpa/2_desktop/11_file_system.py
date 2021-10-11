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
# print(os.path.dirname(r"C:\Users\X0126516\Documents\python\python-rpa\README.md"))

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
# import fnmatch
# pattern = "*.py" #  .py로 끝나는 모든 파일 
# result = []
# for root, dir, files in os.walk("."):
#     for name in files: 
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root, name))

# print(result)
            
# 파일인지 폴더인지 확인 
# print(os.path.isdir("basic"))
# print(os.path.isfile("basic"))

# print(os.path.isdir(".gitignore"))

# # 파일이 존재하는지 확인 
# print(os.path.isfile("aaa"))

# # 주어진 경로가 존재하는지?
# if os.path.exists("rpa_basic"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")

# # 파일 만들기 
# open("new_file.txt", "a").close()

# 파일명 변경하기 
# os.rename("new_file.txt", "new_file_rename.txt")

# 파일 삭제 
# os.remove("new_file_rename.txt")

# 폴더 만들기 
# os.mkdir("new_folder") # 현재 경로 기준으로 생성 (중복된 경우 에러 발생 )

# os.makedirs("new_folders/a/b/c") # 하위폴더 가지는 폴더 생성시도 

# 폴더명 변경 
# os.rename("new_folder", "new_folder_rename")

# 폴더 지우기 
# os.rmdir("new_folder")

# 폴더 포함 하위 내용 지우기 

import shutil 
# shutil.rmtree("new_folders")

# 파일 복사하기 
shutil.copy("README.md", "test_folder") # 원본경로, 대상 경로
shutil.copy("README.md", "test_folder/copied_README.md") # 새 파일명지정가능 
shutil.copyfile("원본파일명", "경로/대상파일명")
shutil.copy2("원본파일명", "경로/대상파일명") # copy와 다른점은 생성일 등의 메타정보도 복사함. 

# 폴더 복사
shutil.copytree("test_folder", "test_folder2") # 원본 , 대상 

# 폴더 이동
shutil.move("test_folder", "test_folder3") # 테스트폴더를 테스트폴더3 폴더 하위에 이동하기, 이동할 폴더명이 존재하지 않는 경우는 폴더명 변경


