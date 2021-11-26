# python-rpa
python-rpa 나도코딩 공부 노트



## RPA 프로그램 종료 방법
 window : ctrl+alt+del  키  / mac : cmd + shift + option + q 

--- 

## RPA 프로그래밍 설치 라이브러리 
 pip install pyautogui openpyxl --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
 pip install pillow --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
 pip install pyperclip 
 pip install selenium  --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
### 메일 관리 
 pip install imap-tools --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
### exe 파일 만들기 
 pip install pyinstaller  --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
 

## exe 파일 만들기 명령어

### 터미널에서 실행하는 프로그램 만들기 
$사용자> pyinstaller .\파일경로

### -F 옵션: 하나의 exe 파일로 압축해주는 실행 프로그램 만들기
$사용자> pyinstaller -F .\파일경로 

### -w 옵션 : 윈도우에서 실행 프로그램 만들기  
$사용자> pyinstaller -w .\파일경로 
$사용자> pyinstaller -w -F .\파일경로 

### --add-data 옵션: 이미지등의 리소스 파일을 명시적으로 추가함 (여러개를 따로 지정해야하는 경우 여러번 반복해서 붙여넣으면 된다.)
#### ".\gui_basic\*.png;gui_basic" : 현재 gui_basic 폴더내에 있는 모든 png파일들을 결과 폴더인 dist/gui_basic 하위에 복사하여 붙여넣기 
$사용자> pyinstaller -w --add-data ".\gui_basic\*.png;gui_basic" -F .\파일경로

### 크롬 로그인해주는 윈도우즈용 프로그램 만들기
pyinstaller -w --add-binary ".\chromedriver.exe;." -F C:\Users\X0126516\Documents\python\python-rpa\ignore\test_site\1_login.py


### 소스에 이미지 등의 경로가 포함된 경우 절대 경로로 반환하도록 수정 
```
# 파일의 절대 경로 반환 
import OS 

def resource_path(relative_path):
    try: 
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
```


--- 

## 크롬 드라이버 설치 
 chrome://version 확인 94.0.4606.71 
 chrome 드라이버 검색하여 설치하기 

--- 

## selenium 메뉴얼 사이트 
https://selenium-python.readthedocs.io/

--- 

## GUI 프로그래밍 t-kinter


## Selenium 시스템에 부착된 장치가 작동하지 않습니다. 에러발생시 해결방법 
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)