# 1 注册200个账号，在前端页面

from selenium import webdriver

b = webdriver.Firefox()

for i in range(1, 200):
    b.get("http://192.168.3.246/ecshop/user.php?act=register")
    b.find_element_by_name("username").send_keys("ts16"+str(i))
    b.find_element_by_name("email").send_keys("165856"+str(i)+"@qq.com")
    b.find_element_by_name("password").send_keys("123456")
    b.find_element_by_name("confirm_password").send_keys("123456")
    b.find_element_by_name("extend_field2").send_keys("123456")
    b.find_element_by_name("extend_field3").send_keys("123456")
    b.find_element_by_name("extend_field4").send_keys("123456")
    b.find_element_by_name("extend_field5").send_keys("123456")
    f = b.find_element_by_name("password").find_element_by_xpath("//option[@value='friend_birthday']")
    f.click()
    b.find_element_by_name("passwd_answer").send_keys("123456")
    b.find_element_by_name("Submit").click()


# 2 输入一个会员，要后台管理页面 删除