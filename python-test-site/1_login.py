from selenium import webdriver
import pyautogui
import time
import tkinter.ttk as ttk
from tkinter import * 
import tkinter.messagebox as msgbox
import sys, os


root = Tk()
root.title("Welcome Site Test Program")
root.geometry("640x480") # 가로세로 길이 


frame_server = Frame(root, relief="flat", bd=0)
frame_server.pack()

Label(frame_server, text="로컬 / 개발 서버 모드").pack()

server_value = StringVar()
server_mode1 = Radiobutton(frame_server, text="로컬", value="http://localhost:8080/", variable=server_value)
server_mode1.select()
server_mode2 = Radiobutton(frame_server, text="개발", value="http://localhost:8082/", variable=server_value)
server_mode1.pack(side="left")
server_mode2.pack(side="left")


frame_user = Frame(root, relief="flat", bd=0)
frame_user.pack(pady="25")
Label(frame_user, text="사용자 유형").pack(side="top")

user_value = StringVar()
user_mode_list = {("관리자", "aq", "1"), \
                    ("관리자", "aa", "1"), \
                    ("관리자", "aa", "1"), \
                    ("관리자", "aa", "1"), \
                    ("관리자", "aa", "1")}

count = 1
for (type, id, pw) in user_mode_list:
    user_button = Radiobutton(frame_user, text=type, value = id+ "####"+pw, variable=user_value)
    user_button.pack()
    if id == "aq": 
        user_button.select()
    
    count += 1


# 로그인아이디 직접 입력하기 

frame_custom = Frame(root, relief="flat", bd=0)
frame_custom.pack(pady="25")
Label(frame_custom, text="로그인아이디").pack()
login_id_custom = Entry(frame_custom, width=30)
login_id_custom.pack()
Label(frame_custom, text="패스워드").pack()
password_custom = Entry(frame_custom, width=30)
password_custom.pack()



def login():
    
    print(user_value.get())
    print(server_value.get())
    
    site = server_value.get()
    
    id = ""
    password = ""
    if login_id_custom.get() == "" and password_custom == "" :
        userAccountInfo = user_value.get().split("####")
        id = userAccountInfo[0]
        password =  userAccountInfo[1]
    else :
        id = login_id_custom.get()
        password =  login_id_custom.get()


    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = ""
    
    if  getattr(sys, 'frozen', False): 
        chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
        browser = webdriver.Chrome(chromedriver_path, options=options)
    else:
        browser = webdriver.Chrome(options=options)
        

    browser.get(site)
    browser.maximize_window()

    print("웹사이트를 열었습니다. ")

    # 로그인 아이디 입력
    elem = browser.find_element_by_id("id")
    elem.send_keys(id)
    pyautogui.sleep(1)
    # 패스워드 입력
    elem = browser.find_element_by_id("password")
    elem.send_keys(password)
    pyautogui.sleep(1)

    # 로그인 버튼 클릭 
    elem = browser.find_element_by_xpath('//*[@id="submit"]')
    elem.click()



button_login = Button(root, text="로그인", command=login)
button_login.pack()
root.mainloop()
