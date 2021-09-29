import pyautogui

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
    moveTabAtFindReplacePopup(1)
    pyautogui.press(convertStringToCharList(newStr))
    moveTabAtFindReplacePopup(7)
    pyautogui.keyDown("enter")   
    pyautogui.keyDown("esc")   
    pyautogui.sleep(1)
    with pyautogui.hold('ctrl'):
        pyautogui.press(['s'])
    pyautogui.sleep(1)
    

# 메인함수 실행 부분 
screen = ""
for w in pyautogui.getAllWindows():
    if 'Spring Tool Suite 4' in w.title:
        screen = w
        print(w.title)

if screen != "":
    screen.activate()
    callFindReplaceText('\<isNotEqual property="([a-z|A-Z|0-9|_]+)" compareValue="([a-z|A-Z|0-9|_|-|@|.]+)"\>', '<if test="$1 ne \'$2\'">' )


    print("정상변경완료!")
    print("정상변경완료!")
    print("정상변경완료!")
    print("정상변경완료!")


print("종료!!")
print("종료!!")
print("종료!!")
print("종료!!")
print("종료!!")