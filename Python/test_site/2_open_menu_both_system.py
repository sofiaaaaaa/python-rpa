import pyautogui
import math

# 레거시사이트와 리뉴얼사이트에서 동시에 같은 화면 열기 

# 메인함수 실행 부분 
screen = ""
# repository = pyautogui.prompt("레파지토리파일명")
for w in pyautogui.getAllWindows():
    if 'Spring Tool Suite 4' in w.title:
        screen = w
        print(w.title)

if screen != "":
    screen.activate()
   
