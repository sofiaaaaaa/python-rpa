import pyautogui
pyautogui.FAILSAFE = False # 사용자의 마우스 조작에 상관없이 코드 실행 
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용 
#마우스 커서 좌표 정보 프로그램 실행됨.
#pyautogui.mouseInfo()

for i in range(10):
    pyautogui.move(100, 100)
    pyautogui.sleep(1)

