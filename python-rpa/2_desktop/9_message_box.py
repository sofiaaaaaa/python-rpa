import pyautogui 

pyautogui.alert("팝업메시지")
result = pyautogui.confirm("컨펌메세지")
print(result)
# 카운트다운 
pyautogui.countdown(3)
print("aa")

result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력")
print(result)

result = pyautogui.password("암호 입력")
print(result)
