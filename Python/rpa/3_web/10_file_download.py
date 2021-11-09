from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 파일 다운로드 경로 
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\X0126516\Documents\python\python-rpa\rpa\3_web'})

browser = webdriver.Chrome(options=chrome_options)
browser.get("http..")

browser.switch_to.frame("iframResult")

# 다운로드 링크 클릭 
elem = browser.find_element_by_xpath('xpath..')

elem.click()

time.sleep(5)
browser.quit()

