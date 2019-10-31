from selenium import webdriver  # 导入selenium

b = webdriver.Firefox()  # 火狐浏览器  # 实例化对象  # 打开浏览器
# b = webdriver.Chrome() # 谷哥浏览器

# 输入网址
b.get("https://www.baidu.com")

# 元素定位

# xpath 相对路径
# b.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
# b.find_element_by_xpath("//span[@class='bg s_ipt_wr quickdelete-wrap']/input").send_keys("selenium")

# 绝对路径
# b.find_element_by_xpath("/html/body/div/div/div/div/div/form/span/input").send_keys("selenium")

# class_name元素定位
# b.find_element_by_class_name("s_ipt").send_keys("selenium1")

# tag元素定位
# b.find_element_by_tag_name("input").click()

# link元素定位
# b.find_element_by_link_text("地图").click()

# partial_link
# b.find_element_by_partial_link_text("地").click()

# name元素定位
# b.find_element_by_name("wd").send_keys("selenium")  # 找到输入信息框元素属性 name=wd 输入值 "selenium"

# id元素定位
# b.find_element_by_id("su").click()     # 找到元素id=su 动作是单击























# id,name,class,tag_name,link,partial_link元素定位：
# b.find_element_by_name("wd").send_keys("你好呀")
# b.find_element_by_id("kw").send_keys("你好呀")
# b.find_element_by_class_name("s_ipt").send_keys("你好呀")
# b.find_elements_by_tag_name("input").send_keys("你好呀")
# b.find_element_by_link_text("新闻").click()
# b.find_element_by_partial_link_text("地").click()

#相对路径
#b.find_element_by_xpath("//form[@id='form']/span/input").send_keys("你好呀")

#绝对路径
#b.find_element_by_xpath("html/body/div/div/div/div/div/form/span/input").send_keys("你好")