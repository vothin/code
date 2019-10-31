# coding=utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
import os


class Ecshop(unittest.TestCase):
    # 初始化数据
    def __init__(self):

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.ecshop_url_1 = "http://192.168.3.246/ecshop/user.php"

    def openbrowse(self, bpath):
        self.bpath = self.driver.get(bpath)
        return self.bpath

    def test_login(self):  # 第一个测试用例
        # 打开主页
        self.driver.get(self.ecshop_url_1)

        # 输入账号密码
        self.driver.find_element_by_name("username").send_keys("ts_test")
        self.driver.find_element_by_name("password").send_keys("123456")

        # 单击登陆
        self.driver.find_element_by_name("submit").click()
        try:
            self.driver.assertTrue(self.driver.find_element_by_xpath("//a[@href='user.php']"), msg="登陆失败")
        except:
            self.save_windows_img()

    # 元素定位的封装
    def ele_id(self, ele_id):
        eleid_1 = self.driver.find_element_by_id(ele_id)
        return eleid_1

    def ele_name(self, ele_name):
        elename = self.driver.find_element_by_name(ele_name)
        return elename

    def ele_xpath(self, ele_xpath):
        elexpath = self.driver.find_element_by_xpath(ele_xpath)
        return elexpath

    def ele_css(self, ele_css):
        elecss = self.driver.find_element_by_class_name(ele_css)
        return elecss

    def ele_select(self, ele_sel):
        ele_sel = Select(self.driver.find_element_by_class_name(ele_sel))
        return ele_sel

    # 验证元素是否存在
    def Check_element(self, type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value)
            return 1
        elif type == "id":
            self.driver.find_element_by_id(value)
            return 1
        elif type == "name":
            self.driver.find_element_by_name(value)
            return 1
        elif type == "link_text":
            self.driver.find_element_by_link_text(value)
            return True
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value)
            return 1

    def open(self, url):

        self.driver.get(url)

    def max_window(self):

        self.driver.maximize_window()

    def set_window(self, wide, high):

        self.driver.set_window_size(wide, high)

    def right_click(self, css):

        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, css):

        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, css):

        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, el_css, ta_css):

        self.element_wait(el_css)
        element = self.get_element(el_css)
        self.element_wait(ta_css)
        target = self.get_element(ta_css)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def click_text(self, text):

        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):

        self.driver.close()

    def quit(self):

        self.driver.quit()

    def submit(self, css):

        self.element_wait(css)
        el = self.get_element(css)
        el.submit()

    def F5(self):

        self.driver.refresh()

    def js(self, script):

        self.driver.execute_script(script)

    def get_attribute(self, css, attribute):

        el = self.get_element(css)
        return el.get_attribute(attribute)

    def get_text(self, css):

        self.element_wait(css)
        el = self.get_element(css)
        return el.text

    def get_display(self, css):

        self.element_wait(css)
        el = self.get_element(css)
        return el.is_displayed()

    def get_title(self):

        return self.driver.title

    def get_url(self):

        return self.driver.current_url

    # 截图日志，存放在Error_Picture路径下
    def save_windows_img(self):
        image_path = os.path.join(r'C:\Users\Administrator\PycharmProjects\ts16\day8\Error_Picture\\')
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        image = image_path + now + ".png"
        time.sleep(1)
        try:
            self.driver.get_screenshot_as_file(image)
        except:
            self.save_windows_img()

    def wait(self, secs):

        self.driver.implicitly_wait(secs)

    def accept_alert(self):

        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css):
        '''
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("css=>#el")
        '''
        self.element_wait(css)
        iframe_el = self.get_element(css)
        self.driver.switch_to.frame(iframe_el)

    def switch_to_frame_out(self):

        self.driver.switch_to.default_content()

    def open_new_window(self, css):

        original_windows = self.driver.current_window_handle
        el = self.get_element(css)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver.switch_to.window(handle)
