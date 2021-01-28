# coding = utf-8
# 导包：selenium\延时关闭
# 获取浏览器对象
#打开本地路径：
#查找元素,输入 用户名：admin 密码：123456
#暂停三秒
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# # r“ acc/” r:修饰的字符串，若含有转义字符，不进行转义操作
# # 使用//也可取消转义操作
# # 也可直接复制浏览器地址，不用管乱码
# url = r"D:\学习资料\Python学习\自动化测试\讲义\web自动化_day01_课件+笔记+资料+代码\02_其他资料\浏览器\课堂素材\注册A.html"
# driver.get(url)
# username = driver.find_element_by_id("userA")
# password = driver.find_element_by_id("passwordA")
# username.send_keys("admin")#用户名输入
# password.send_keys("123456")
# sleep(3)

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
search_content = driver.find_element_by_id("kw")
search_content.send_keys("hello")
sleep(3)

driver.quit()
#
