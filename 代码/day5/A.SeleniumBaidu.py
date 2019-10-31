from selenium import webdriver  # 导入selenium

b = webdriver.Firefox()  # 火狐浏览器  # 实例化对象  # 打开浏览器
# b = webdriver.Chrome() # 谷哥浏览器

# 输入网址
b.get("https://www.baidu.com")

# 元素定位

# class_name元素定位
b.find_element_by_class_name("s_ipt").send_keys("selenium1")

# name元素定位
b.find_element_by_name("wd").send_keys("selenium")  # 找到输入信息框元素属性 name=wd 输入值 "selenium"

# id元素定位
b.find_element_by_id("su").click()     # 找到元素id=su 动作是单击