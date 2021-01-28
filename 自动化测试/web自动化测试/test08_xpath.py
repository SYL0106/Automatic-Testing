
from selenium import webdriver
from time import sleep

# driver = webdriver.Ie()
# # driver = webdriver.Chrome()
# url = r"C:\Users\Administrator\Desktop\注册A.html"
# driver.get(url)
# driver.maximize_window()
# driver.find_element_by_name("userA").send_keys("admin")
# sleep(5)


driver = webdriver.Ie()
url = r"C:\Users\Administrator\Desktop\注册A.html"
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath("/html/body/form/div/fieldset/p[1]/input").send_keys("admin")

# xpath 相对路径与逻辑结合定位元素
driver.find_element_by_xpath("//input[@name = 'passwordA' and @placeholder = '密码A']").send_keys("123")


# xpath 层级结合属性定位账号A
driver.find_element_by_xpath("//p[@id = 'p1']/input").send_keys("110")
sleep(2)
# xpath //*[text() = '']
#//*[contains(@attribute,'')]
# //*[start-with(@attribute,'')]

driver.quit()
