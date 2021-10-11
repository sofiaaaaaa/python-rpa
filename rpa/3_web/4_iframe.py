from selenium import webdriver
import time

browser = webdriver.Chrome()

# w3school 연습페이지 이동
browser.get('')

# 프레임전환 
browser.switch_to.frame('iframeResult')

# xpath로 iframe 내 태그 접근
elem = browser.find_element_by_xpath('//')

elem.click()

# 상위로 빠져나옴
browser.switch_to.default_content()

# 5초 대기 
time.sleep(5)

browser.quit()

