'''
 记录cookie
通过向浏览器中添加cookie可以绕过登录的验证码。在登录的时候勾选记住密码，当下次访问该网站时就默认处于登录状态了。
记住密码功能其实就记录了浏览器的cookie中。通过webdriver来操作浏览器的cookie，可以通过add_cookie()方法将用户名密码写入浏览器cookie，
当再次访问时，服务器将直接读取浏览器的cookie进行登录。
cookie处理：
get_cookies()
     获得所有cookie信息
get_cookie(name)
     返回特定name 有cookie信息
add_cookie(cookie_dict)
     添加cookie，必须有name 和value 值
delete_cookie(name)
     删除特定(部分)的cookie信息
delete_all_cookies()
     删除所有cookie信息
'''

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://192.168.2.246/ecshop/user.php")

# 获取cookie
cookies = driver.get_cookies()
cookiename = driver.get_cookie(name="ECS_ID")
print(cookies)
print(cookiename)

# 遍历cookie
for cookiefor in driver.get_cookies():
    print("name=%s,value=%s" %(cookiefor["name"],cookiefor["value"]))
print()

# 增加cookie
driver.add_cookie({"name": "name", "value": "value"})
cookieadd = driver.get_cookies()
print(cookieadd)
for cookiefor in driver.get_cookies():
    print("name=%s,value=%s" %(cookiefor["name"],cookiefor["value"]))
print()

# 删除cookie
driver.delete_cookie(name="ECS_ID")
cookiedel = driver.get_cookies()
print(cookiedel)
for cookiefor in driver.get_cookies():
    print("name=%s,value=%s" %(cookiefor["name"],cookiefor["value"]))
print()

# 全部删除
driver.delete_all_cookies()
cookie_del_all = driver.get_cookies()
print(cookie_del_all)
