import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://daum.net")

# 프레임 전환
browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('//*[@id="male"]')

if elem.is_selected() == False : 
    elem.click();

time.sleep(5)

browser.quit()
