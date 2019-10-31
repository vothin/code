from selenium import webdriver
import time

b = webdriver.Firefox()
b.get("http://192.168.3.246/ecshop/admin/privilege.php?act=login")

b.find_element_by_name("username").send_keys("admin")
b.find_element_by_name("password").send_keys("a1234567")
b.find_element_by_xpath("//input[@class='btn-a']").click()


b.switch_to_frame("menu-frame")
b.find_element_by_link_text("广告列表").click()

b.switch_to_default_content()

b.switch_to_frame("main-frame")


checks = b.find_elements_by_xpath("//img[@src='images/icon_edit.gif']")
checks[0].click()
# b.find_element_by_id("selbtn1").click()

# 删除只读属性
js = "document.getElementById('start_time').removeAttribute('readonly')"
b.execute_script(js)

# 删除先前的内容
b.find_element_by_id('start_time').clear()   # clear:清除内容

# 输入新的日期
b.find_element_by_id('start_time').send_keys('2016-08-24')
time.sleep(2)

