import pyautogui

# 스크린샷 
# img = pyautogui.screenshot()
# img.save("screenshot.png")

# rgb값 리턴 
pixel = pyautogui.pixel(28, 18)
print(pixel)

# 버튼 색을 저장해놨다가 색이 동일한지 확인 하는 용도로 사용할 수 있음 
pyautogui.pixelMatchesColor(28, 18, (21,153,233))
