from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://m-flight.naver.com/?gclid=EAIaIQobChMIoITK1c3X8wIVT7eWCh3UvwcvEAAYASAAEgJx2fD_BwE')

browser.find_element_by_partial_link_text('가는날 선택').click()
browser.find_elements_by_link_text('30')[0].click() # 현재달 30일 선택

browser.find_elements_by_link_text('5')[1].click() #  다음달 5일 선택

# 제주도 클릭 
browser.find_element_by_xpath('xpath..').click()

# 항공권 검색 클릭 
browser.find_elements_by_link_text('항공권 검색').click()

try: 
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, 'xpath..')))
    print(elem.text) # text부분 출력 
except: 
    print("실패했어요")

# 첫번째 결과 출력 
# elem = browser.find_element_by_xpath('xpath..')

# print(elem.text) # text부분 출력 




time.sleep(5)
browser.quit()
