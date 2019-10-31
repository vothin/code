from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://192.168.3.246/ecshop/user.php?act=register")
time.sleep(3)

# 移动底部
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)

# 将滚动条移动到页面的顶部
time.sleep(3)
js_ = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js_)

# 用户名的颜色变成红色
jsname = "var q=document.getElementById(\"username\");q.style.border=\"1px solid red\";"

# 调用js
driver.execute_script(jsname)











































#print(driver.execute_script("document.title"))
#
# def scroll_top():
#     if driver.name == "chrome":
#         js = "var q=document.body.scrollTop=0"
#
#     else:
#         js = "var q=document.documentElement.scrollTop=0"
#         return driver.execute_script(js)
#
# # 拉到底部
# def scroll_foot():
#
#
#     if driver.name == "chrome":
#         js = "var q=document.body.scrollTop=10000"
#     else:
#         js = "var q=document.documentElement.scrollTop=10000"
#         return driver.execute_script(js)
# # 聚焦元素
# target = driver.find_element_by_xxxx()
# driver.execute_script("arguments[0].scrollIntoView();", target)
