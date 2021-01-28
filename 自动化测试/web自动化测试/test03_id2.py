from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
search_content = driver.find_element_by_id("kw")
search_content.send_keys("hello")
sleep(5)

driver.quit()