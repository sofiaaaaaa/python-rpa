import time
from selenium import webdriver
from selenium.wedriver.common.action_chains  import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

time.sleep(5)

# 특정 영역 스크롤 
elem = browser.find_element_by_xpath('xpath .. ')

# 방법1 Action chain
actions = ActionChains(browser)
actions.move_to_element(elem).perform()

# 방법2 좌표정보 이용 
xy = elem.location_once_scrolled_into_view 
print("type : ", type(xy))
print("value: ", xy)

elem.click()


time.sleep(5)
browser.quit()
