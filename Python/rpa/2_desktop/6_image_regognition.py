from PIL.ImageOps import grayscale
import pyautogui

# 버튼이미지캡처파일과 비교해서 좌표를 찾아 클릭함
# file_menu = pyautogui.locateOnScreen("file_menu.png")

# print(file_menu)

# pyautogui.click(file_menu)

# for i in pyautogui.locateAllOnScreen("file_menu.png"):
#     print(i)
#     pyautogui.click(i, duration=2)



# 검색 속도를 높이는 방법 
# 1. Gray Scale 

# file_menu = pyautogui.locateOnScreen("file_menu.png", grayscale=True)
# pyautogui.moveTo(file_menu)

# 2. 범위 지정
# pyautogui.moseInfo()
# file_menu = pyautogui.locateOnScreen("file_menu.png", region=(x,y,width,height))
# pyautogui.moveTo(file_menu)

# window키 + shift + s 조합 : 스크린 캡처