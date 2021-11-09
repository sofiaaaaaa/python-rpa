from selenium import webdriver
from selenium.webdriver.common.by import By 

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('http...')
browser.switch_to.frame("iframe id..")
elem = browser.find_element_by_xpath('xpath')

if elem.is_selected() == False:
    elem.click()

elem = browser.find_element(By.XPATH, 'xpath..')

browser.quit()