from selenium import webdriver
import time

b = webdriver.Firefox()
b.get("http://www.hao123.com/")

# 获取当前窗口的句柄--搜主页
nowhandle = b.current_window_handle  # 当前主页的句柄  hao123的句柄
print(nowhandle)

b.find_element_by_link_text("贴吧").click()   # 点击贴吧链接
nowhandle1 = b.current_window_handle #获取贴吧窗口的句柄   贴吧的句柄

time.sleep(3)
allhandle = b.window_handles

for handle in allhandle:
    if handle != nowhandle:
        b.switch_to_window(nowhandle)   # 切换到hao123句柄  nowhandle
        time.sleep(3)

b.quit()

