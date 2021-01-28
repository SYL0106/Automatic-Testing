from selenium import webdriver
from time import sleep

#driver = webdriver.Chrome()
driver = webdriver.Ie()
driver.get("http://www.baidu.com")
sleep(3)
driver.quit()


