import pyautogui
import math

# 서비스임플 소스 정리하기 
# 프로그램 실행시 주의사항 
# 1. capslock버튼 비활성화하기 

# 문자열을 문자 배열로 반환 
def convertStringToCharList(str):
    word = str
    lst = []

    for i in word:
        lst.append(i)

    return lst

# 텍스트 찾기 창 열기 
def openFindReplacePopup():
    with pyautogui.hold('ctrl'):
        pyautogui.press(['f'])
    #pyautogui.hotkey('ctrl', 'shift', 'esc')

def moveTabAtFindReplacePopup(max):
    for i in range(0, max):
        pyautogui.keyDown("\t")

# text find / replace 
def callFindReplaceText(condition, newStr):
    openFindReplacePopup()
    pyautogui.press(convertStringToCharList(condition))
    pyautogui.sleep(2)
    moveTabAtFindReplacePopup(1)
    if newStr == "":
        pyautogui.keyDown("backspace")
    else:
        pyautogui.press(convertStringToCharList(newStr))

    moveTabAtFindReplacePopup(7)
    pyautogui.keyDown("enter")   
    pyautogui.keyDown("esc")   
    pyautogui.sleep(1)
    with pyautogui.hold('ctrl'):
        pyautogui.press(['s'])
    pyautogui.hotkey("ctrl","home") # 커서맨앞
    pyautogui.sleep(1)

# text find / replace - Array 파라미터
def callFindReplaceByArray(conditionArray, newStrArray):
    openFindReplacePopup()
    pyautogui.press(conditionArray)
    pyautogui.sleep(1)
    moveTabAtFindReplacePopup(1)
    if newStrArray == "":
        pyautogui.keyDown("backspace")
    else:
        pyautogui.press(newStrArray)

    moveTabAtFindReplacePopup(7)
    pyautogui.keyDown("enter")   
    pyautogui.keyDown("esc")   
    pyautogui.sleep(1)
    with pyautogui.hold('ctrl'):
        pyautogui.press(['s'])
    pyautogui.hotkey("ctrl","home") # 커서맨앞
    pyautogui.sleep(1)


def formatterJavaCode():
    pyautogui.hotkey("ctrl","a")
    pyautogui.hotkey("ctrl","shift","f")
    pyautogui.hotkey("ctrl","shift","o")

def loopTask(tasklist):
    listCount = len(tasklist)
    count = 0
    print("Progress : " , end="")   

    for before, after in tasklist:
        callFindReplaceText(before, after)
        count += 1
        displayProgress(count, listCount)
    print()

# 진행바표시 
def displayProgress(count, listCount):
   
    progressRatio = round(count/listCount * 100)
    print(str(progressRatio) +"%")

    # if previousRatio < progressRatio: 
    #     progressbar = "■"
    #     # progressbar += loopText("□", 10-progressRatio)
    #     print(progressbar , end="")    

    # return progressRatio


# 텍스트 지정횟수만큼 반복하여 반환 
def loopText(text, count): 
    result = ""
    for i in range(count):
        result += text
    return result

# # 한글입력
# def copyPasteHangul(text):
#     pyperclip.copy(text)
#     pyautogui.hotkey("ctrl", "v")
    

# 메인함수 실행 부분 
screen = ""
repository = pyautogui.prompt("레파지토리파일명")
for w in pyautogui.getAllWindows():
    if 'Spring Tool Suite 4' in w.title:
        screen = w
        print(w.title)

if screen != "":
    screen.activate()
    task = [
             ('xxxxxxxxxxxxxxxxx',  'vvvvvvvvvv'),
    ]
    loopTask(task)


    # try catch문 띄어쓰기
    # print(convertStringToCharList("return rtnList;"))


    # 코드 정리 
    formatterJavaCode()

    print("정상변경완료!")



print("종료!!")
print("종료!!")