#내장함수.

# input 사용자의 입력을 받는 함수 

# dir 어떤 객체를 받을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시함 

import random
import pickle
print(dir())

print(dir(random))

list = [1,2,3]

print("list" , dir(list))

# 외장함수. import해서 쓰는 모듈들. random, shuffle 등 

import glob

print(glob.glob("*.py")) # 현재 파일 경로 내에 확장자가 py인 모든 파일의 목록조회

# 운영체제 제공하는 기본 기능 
import os 
print(os.getcwd()) # 현재 디렉토리 

folder = "sample"

if os.path.exists(folder):
    print("already exists.")
    os.rmdir(folder)
else: 
    os.makedirs(folder)
    print("folder ..", folder)

import time
print(time.localtime())
print(time.strftime("%Y-%m %d %H:%M:%S"))

import datetime
print("today .. ", datetime.date.today())

# timedelta 
today = datetime.date.today()
td = datetime.timedelta(days=100)

print("aa ", today+td)