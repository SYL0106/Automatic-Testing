from selenium import webdriver
from time import sleep

#-------------------

# 1. css id选择器定位用户名 输入admin
# 2. css 属性选择器 定位密码框 输入123456
# 3. css class 选择器定位电话号码 输入17300001111
# 4. css 元素 选择器 定位span标签获取文本值
# 5. css 使用层级选择器定位email 输入123@qq.com

#-------------------


driver = webdriver.Ie()
url = r"C:\Users\Administrator\Desktop\注册A.html"
driver.get(url)
# 1
driver.find_element_by_css_selector("#userA").send_keys("admin")
# 2
driver.find_element_by_css_selector("[name = 'passwordA']").send_keys("123456")
# 3
driver.find_element_by_css_selector(".telA").send_keys("17300001111")
# 4
span = driver.find_element_by_css_selector("span").text
# 5
driver.find_element_by_css_selector("p > input[placeholder = '电子邮箱A']").send_keys("123@qq.com")

print(span)
sleep(5)
driver.quit()
