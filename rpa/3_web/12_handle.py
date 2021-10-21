from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://m-flight.naver.com/?gclid=EAIaIQobChMIoITK1c3X8wIVT7eWCh3UvwcvEAAYASAAEgJx2fD_BwE')

curr_handle = browser.current_window_handle

print(curr_handle)

# 다른 화면 새탭에 띄우기 
browser.find_element_by_xpath('xpath..').click()

handles = browser.window_handles # 모든 핸들 정보 

for handle in handles:
    print(handle)
    # 브라우저 전환 
    browser.switch_to.window(handle) # 각 핸들로 이동함 
    print(browser.title) # 현재 브라우저(핸들)의 제목 표시 


# 현재 핸들 닫기 
browser.close()

# 이전 핸들로 돌아오기 
print("처음으로 돌아오기")
browser.switch_to.window(curr_handle)

print(browser.title)

time.sleep(5)
browser.get('http:daum.net')


time.sleep(5)
browser.quit()
