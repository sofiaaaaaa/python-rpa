import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]

w.activate()

# pyautogui.write("12345")
# pyautogui.write("abcde", interval=1)
# pyautogui 만으로는 한글처리가 안됨

# automatetheboringstuff.com 사이트 참조 
# pyautogui.write(["t", "e", "s", "left", "right","l","a","enter"], interval=0.6)

# #특수문자 
# # shift 4 -> $
# pyautogui.keyDown("shift") #  shift키를 누른 상태에서  
# pyautogui.press("4") # 4입력
# pyautogui.keyUp("shift") # shift 키 떼기 

# # 조합키 (Hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl") # Ctrl + A


# # 간편한 조합키 
# pyautogui.hotkey("ctrl", "alt", "shift", "a")

# pyautogui.hotkey("ctrl", "a")


# 한글 입력


import pyperclip

pyperclip.copy("한글") # 글자를 클립보드에 저장 
pyautogui.hotkey("ctrl", "v") # 클립보드 내용 붙여넣기 

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")