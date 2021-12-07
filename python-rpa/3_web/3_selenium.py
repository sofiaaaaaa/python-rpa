from selenium import webdriver

# browser = webdriver.Chrome("./chromedriver.exe")

browser = webdriver.Chrome()
browser.get("http://daum.net")# elem = browser.find_element_by_link_text("카페")# print(elem.get_attribute("href"))# elem.click()# browser.back()# browser.forward()# browser.refresh()

# elem = browser.find_element_by_id("q")# elem.send_keys("abcd")

# from selenium.webdriver.common.keys
import Keys

# elem.send_keys(Keys.ENTER)

# 단건
elem = browser.find_element_by_tag_name("a")

elem.get_attribute('href')

# 여러개
elems = browser.find_elements_by_tag_name("a")

for e in elems:
    print(e.get_attribute("href"))

# 페이지 이동 
browser.get("http://daum.net")

elem = browser.find_element_by_name("q")
elem.send_keys("aaaa")
elem.clear() # 입력내용 지우기 
elem.send_keys("bbbb")
elem = browser.find_element_by_xpath('//*[@id="input"]')
elem.click()

# 스크린샷 저장 
browser.save_screenshot('daum.png')

# 현재 탭 종료 
browser.close()

# 브라우저 전체 종료 
browser.quit()

# 브라우저 소스 확인 
browser.page_source()