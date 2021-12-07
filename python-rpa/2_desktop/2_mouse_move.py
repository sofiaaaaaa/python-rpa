import pyautogui

# 절대좌표
# 왼쪽상단으로부터 x,y 만큼 마우스 이동
# pyautogui.moveTo(100, 100)
# 5초 동안 이동
pyautogui.moveTo(100,200, duration = 5)
print(pyautogui.position())
# 상대좌표로 이동 (현재 커서위치를 시작점으로 하여 이동함)
pyautogui.move(100,100, duration=5)
print(pyautogui.position())

p = pyautogui.position()
print(p.x, p.y, p[0], p[1])


