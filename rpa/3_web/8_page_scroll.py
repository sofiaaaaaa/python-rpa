from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('http...')

# 무선마우스 라고 입력함 
elem = browser.find_element_by_xpath('xpath..')
time.sleep(1)
elem.send_keys('무선마우스')
time.sleep(1)

elem.send_keys(Keys.ENTER)

# 검색버튼 클릭을 위해 엔터처리 
# browser.find_element_by_xpath('xpath..').click()

# 스크롤 
# 모니터해상도 높이인 1080 위치로 스크롤 이동함  
# browser.execute_script("window.scrollTo(0, 1080)") # 1920* 1080 해상도에 따라 설정하기 


# 화면의 가장 아래로 스크롤 내리기 
# pagedown 버튼은 한페이지씩 내리고, end버튼은 끝까지 스크롤 
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")


time.sleep(5)

browser.quit()

