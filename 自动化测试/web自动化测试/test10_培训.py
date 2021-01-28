# coding:utf-8
from selenium import webdriver
from time import sleep

driver = webdriver.Ie()
url = r"http://www.baidu.com"
driver.get(url)
# sleep(3)
driver.refresh()
url = "http://www.bresee.cn/"
driver.get(url)
# 设置指定的窗口大小（540，960）
driver.set_window_size(540,960)
# sleep(3)
# 窗口最大化
driver.maximize_window()
print("已全屏")
sleep(3)
# 截屏
lo_url = r"C:\Users\Administrator\Desktop\a.png"
driver.get_screenshot_as_file(lo_url)
print("已截图完成")




sleep(2)
driver.quit()


