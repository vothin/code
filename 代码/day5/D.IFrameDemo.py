from selenium import webdriver
import time

b = webdriver.Firefox()

b.get("http://192.168.3.246/ecshop/admin/privilege.php?act=login")

# 账号密码
b.find_element_by_name("username").send_keys("admin")
b.find_element_by_name("password").send_keys("a1234567")

# 登陆
b.find_element_by_xpath("//input[@class='btn-a']").click()

# header-frame
b.switch_to_frame("header-frame")
b.find_element_by_xpath("//a[@href='comment_manage.php?act=list']").click()


# 跳出默认的帧
b.switch_to_default_content()


# 跳帧 menu-frame
b.switch_to_frame("menu-frame")
b.find_element_by_link_text("商品列表").click()

# 跳出默认的帧
b.switch_to_default_content()

# main-frame
b.switch_to_frame("main-frame")

checkboxes = b.find_elements_by_name("checkboxes[]")
for i in checkboxes:
    i.click()
