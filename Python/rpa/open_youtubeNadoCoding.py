#https://www.youtube.com/watch?v=exgO1LFl9x8

#https://www.youtube.com/watch?v=bKPIcoou9N8


# 메인함수 실행 부분 

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.youtube.com/watch?v=bKPIcoou9N8")
elem = browser.find_element_by_xpath('//*[@id="movie_player"]/div[32]/div[2]/div[1]/button')
elem.click()