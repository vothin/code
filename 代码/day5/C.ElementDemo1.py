from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标事件
from selenium.webdriver.common.keys import Keys   # 键盘事件

b = webdriver.Chrome()  # 实例化对象

b.get("https://www.baidu.com")  #登陆


'''
  context_click()  右击
  double_click()   双击
  drag_and_drop()  拖动
  move_to_element()  鼠标悬停在一个元素上
  click_and_hold()   按下鼠标左键在一个元素上
'''

# 右击
# c_click = b.find_element_by_link_text("新闻")
# ActionChains(b).context_click(c_click).perform()


# 双击
# b.find_element_by_id("kw").send_keys("selenium1")
# d_click = b.find_element_by_id("kw")
# ActionChains(b).double_click(d_click).perform()

# 悬停
# move =b.find_element_by_link_text("设置")
# ActionChains(b).move_to_element(move).perform()

# 拖动

move1 = b.find_element_by_name("username")
# move1_v = move1.send_keys("你好呀")
#
# ActionChains(b).double_click(move1).perform()
#
# move2 = b.find_element_by_name("email")
# ActionChains(b).drag_and_drop(move1, move2).perform()


# 按下左键
dragger = b.find_element_by_link_text("设置")
ActionChains(b).click_and_hold(dragger).release(move1).perform()






# b.find_element_by_id("kw").send_keys("selenium1")
# time.sleep(2)
# b.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)  # 删除一格
# # b.find_element_by_id("kw").send_keys(Keys.TAB, Keys.TAB)
# # b.find_element_by_id("kw").send_keys(Keys.SPACE)
# time.sleep(3)
# #b.find_element_by_id("kw").send_keys(Keys.ESCAPE)
# b.find_element_by_id("kw").send_keys(Keys.ENTER)   # 回车
#
# # 全选,复制,剪切,粘贴
# b.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')  # 全选
# time.sleep(3)
# b.find_element_by_id("kw").send_keys(Keys.CONTROL, 'c')  # 复制
# b.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
# b.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')  # 粘贴
# time.sleep(3)
#
# b.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')  # 剪切
# time.sleep(3)
#
#
#
# time.sleep(10)
# b.quit()



# CSS定位
# b.find_element_by_css_selector("#kw").send_keys("selenium")
# b.find_element_by_css_selector(".s_ipt").send_keys("selenium1")

#  标签idclass.. > 标签 > 标签
# b.find_element_by_css_selector("form#form > span > input ").send_keys("selenium")
# b.find_element_by_css_selector("input[autocomplete='off']").send_keys("selenium2")

#
# 最大小，定制窗口大小
# b.maximize_window()
# time.sleep(2)
# b.set_window_size(500, 600)
# time.sleep(2)
#
# # 标题,URL
# print("这是标题：", b.title)
# print("这是URL", b.current_url)
#
# # 后退与前进
# b.find_element_by_link_text("地图").click()
# time.sleep(2)
# b.back()
# time.sleep(3)
# b.forward()


# 尺寸,文本值,属性,可用状态
# print(b.find_element_by_id("kw").size)  #输出这个元素的尺寸
#
# print(b.find_element_by_name("tj_trnews").text)
#
# print(b.find_element_by_id("kw").get_attribute("type"))
#
# print(b.find_element_by_id("kw").is_displayed())



'''
sleep()： 强制等待，设置固定休眠时间。 python 的 time 包提供了休眠方法 sleep() ， 
导入 time 包后就可以使用 sleep()，进行脚本的执行过程进行休眠。

implicitly_wait()：隐石等待，也叫智能等待，
是 webdirver 提供的一个超时等待。隐的等待一个元素被发现，或一个命令完成。如果超出了设置时间的则抛出异常。

WebDriverWait()：显示等待，同样也是 webdirver 提供的方法。在设置时间内，
默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常。
默认检测频率为0.5s，默认抛出异常为：NoSuchElementException
'''








































#







# b.find_element_by_name("username").send_keys("ts16")  #账号
# time.sleep(1)
# b.find_element_by_name("password").send_keys("123456") #密码
# time.sleep(2)
# b.find_element_by_xpath("//input[@class='us_Submit']").click()








# b.quit()   #退出