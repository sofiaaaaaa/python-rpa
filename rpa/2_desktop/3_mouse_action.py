import pyautogui

# 3초 대기 
# pyautogui.sleep(3)
# print(pyautogui.position())

# 클릭
# pyautogui.click(-2803, -507, duration=1)
# click = mousedown + mouseup 
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# double click 
# pyautogui.doubleClick()
# pyautogui.click(clicks=2)

# # drag an drop
# pyautogui.moveTo(100, 100)
# pyautogui.mouseDown(200, 300)
# pyautogui.moveTo(100,200)
# # pyautogui.mouseUp()

# pyautogui.sleep(3)
# pyautogui.rightClick()
# pyautogui.middleClick()

# 상대좌표
# pyautogui.drag(100, 100, duration=5)

# 절대좌표 drag 
# pyautogui.dragTo(100, 200)

# scroll 위방향으로
pyautogui.scroll(300)

pyautogui.scroll(-300)