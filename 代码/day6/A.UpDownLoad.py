from selenium import webdriver
import time


b = webdriver.Firefox()
b.get("http://192.168.3.246/ecshop/user.php")

b.find_element_by_name("username").send_keys("ts161")
b.find_element_by_name("password").send_keys("123456")
b.find_element_by_name("submit").click()

time.sleep(3)
# 用户中心
b.find_element_by_xpath("//a[@href='user.php']").click()
time.sleep(1)
# 我的留言
b.find_element_by_xpath("//a[@href='user.php?act=message_list']").click()
time.sleep(1)

# 上传

# 投诉
b.find_element_by_xpath("//input[@value='1']").click()

time.sleep(1)
# 主题
b.find_element_by_name("msg_title").send_keys("我想上传呀")
time.sleep(1)
# 留言内容
b.find_element_by_name("msg_content").send_keys("我想上传呀")
time.sleep(1)
# 上传图片
b.find_element_by_name("message_img").send_keys(r"C:\Users\Administrator\Desktop\每日一讲.png")
time.sleep(1)
b.find_element_by_class_name("bnt_bonus").click()






























# 下载
# fp = webdriver.FirefoxProfile()  # 设置一些相关的操作
# fp.set_preference("browser.download.folderList", 2)  # 设置Firefox的默认 下载 文件夹。0是桌面；1是“我的下载”；2是自定义
# fp.set_preference("browser.download.manager.showWhenStarting", False)  # 是否使用默认路径下载
# fp.set_preference("browser.download.dir", os.getcwd())  # 设置当前路径为下载地址
# print(os.getcwd())
# fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream, application/vnd.ms-excel, text/csv, application/zip,application/xml");
#
# #不会弹出警告框
# fp.set_preference("browser.download.manager.alertOnEXEopen", False)
# fp.set_preference("browser.download.manager.focusWhenStarting", False)
# fp.set_preference("browser.download.manager.useWindow", False)
# fp.set_preference("browser.download.manager.showAlertOnComplete", False)
# fp.set_preference("browser.download.manager.closewhenDone", False)
#
# browser = webdriver.Firefox(firefox_profile=fp)
# browser.get("https://www.python.org/downloads/release/python-370/")
# browser.find_element_by_partial_link_text("Windows x86-64 embed").click()
# time.sleep(3)
# alert_1 = browser.switch_to_alert()
# alert_1.accept()

# browser.close()

