import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창 
# print(fw.title)
# print(fw.size)
# print(fw.left, fw.top, fw.right, fw.bottom)
# pyautogui.click(fw.left + 40, fw.top + 20)

# 모든 윈도우 가져오기 
for w in pyautogui.getAllWindows():
    print(w)

for w in pyautogui.getWindowsWithTitle("제목 없음"):
    print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)

# 맨앞으로 화면 가져오기 
if w.isActive == False:
    w.activate()

# 화면 최대화 <-> minimize()
if w.isMaximized == False:
    w.maximize()

pyautogui.sleep(3)

# 화면 상태 기존으로 원복 
w.restore()

# 윈도우 닫기 
w.close()