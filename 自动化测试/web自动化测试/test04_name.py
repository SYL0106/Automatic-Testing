from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_name("wd").send_keys("hello")
sleep(3)
driver.quit()


