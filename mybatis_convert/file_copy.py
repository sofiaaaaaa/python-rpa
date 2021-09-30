import pyautogui

# 프로그램 실행시 주의사항 
# 1. capslock버튼 비활성화하기 

# file copy 
def fileCopyTo(folerName, serviceList):
    servicePath = ""
    dummyFileName = ""
    pyautogui.write("cd "+ servicePath + folerName)
    pyautogui.press("enter")
    for service in serviceList:
        service = service.replace("DU_","")
        service = service.replace(".java","Service.java")
        pyautogui.write("cp "+ servicePath + dummyFileName + " " + service)
        pyautogui.press("enter", interval=1)

    pyautogui.write("ls")
    pyautogui.press("enter")

# 메인함수 실행 부분 
windowName = "Windows PowerShell"
screen = ""
for w in pyautogui.getAllWindows():
    if windowName in w.title:
        screen = w
        print(w.title)

if screen != "":
    screen.activate()
    # fileCopyTo("",[""])
    print("정상변경완료!")


print("종료!!")