from selenium import webdriver
import time 

browser = webdriver.Chrome()
browser.get('http...')
browser.switch_to.frame("iframeResult   iframe id")

elem = browser.find_element_by_xpath("xpath.")
elem.click()

time.sleep(5)

# 텍스트 일치 
elem = browser.find_element_by_xpath("xpath  /option[text()='ABC']")

# 텍스트값 부분 일치 
elem = browser.find_element_by_xpath("xpath  /option[contains(text(),'ABC')]")


browser.quit()