from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('http...')

# 무선마우스 라고 입력함 
# elem = browser.find_element_by_xpath('xpath..')
# time.sleep(1)
# elem.send_keys('무선마우스')
# time.sleep(1)

# elem.send_keys(Keys.ENTER)

# 검색버튼 클릭을 위해 엔터처리 
# browser.find_element_by_xpath('xpath..').click()

# 스크롤 
# 모니터해상도 높이인 1080 위치로 스크롤 이동함  
# browser.execute_script("window.scrollTo(0, 1080)") # 1920* 1080 해상도에 따라 설정하기 


# 화면의 가장 아래로 스크롤 내리기 
# pagedown 버튼은 한페이지씩 내리고, end버튼은 끝까지 스크롤 
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")


# 동적 페이지에 대해 마지막까지 스크롤 반복 수행
# 2초에 한번씩 스크롤 내리기 
interval = 2

# 현재 문서 높이를 가져와서 저장 
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복수행
while True:
    # 스크롤을 화면 가장 아래로 내리기 
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight")

    # 페이지 로딩 대기 
    time.sleep(interval)

    # 현재 문서 높이 가져와서 저장 
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height: # 직전 높이와 같으면, 높이 변화가 없으면 반복문 탈출 
        break

    prev_height = curr_height


# 브라우저 맨 위로 올리기 
browser.execute_script("window.scrollTo(0, 0)") # 1920* 1080 해상도에 따라 설정하기 


time.sleep(5)

browser.quit()

