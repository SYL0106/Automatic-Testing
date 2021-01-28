from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# driver = webdriver.Ie()
url_1 = 'https://www.baidu.com/'
driver.get(url_1)
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").submit()
driver.find_element_by_id("su").click()
# driver.find_element_by_link_text("hao123").click()
# url_2 = 'http://news.baidu.com/'
# driver.get(url_2)
# driver.find_element_by_tag_name("_blank").click()

print("新闻页")
sleep(3)
driver.back()


#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input").send_keys("xpath")
#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/div/form/span[2]/input").click()

sleep(5)


driver.quit()

