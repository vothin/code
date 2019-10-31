from selenium import webdriver
import time

b = webdriver.Firefox()
b.get("http://192.168.2.246/ecshop/user.php")

b.find_element_by_name("username").send_keys("sz")
b.find_element_by_name("submit").click()

alert_1 = b.switch_to_alert()
alerttext = alert_1.text
time.sleep(2)
alert_1.accept()
print(alerttext)
