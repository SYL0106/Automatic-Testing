from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)
driver.find_element_by_tag_name("input").send_keys("selenium")
sleep(3)
driver.quit()

