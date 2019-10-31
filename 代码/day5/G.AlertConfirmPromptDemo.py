from selenium import webdriver
import time

b = webdriver.Firefox()

'''
alert/confirm/prompt处理：

switch_to_alert()
    用于获取网页上的警告信息。
text			
     返回 alert/confirm/prompt 中的文字信息。
accept		
     点击确认按钮。
dismiss		
     点击取消按钮，如果有的话。
send_keys	
    输入值，这个alert\confirm没有对话框就不能用了，不然会报错
'''

b.get("file:///C:/Users/Administrator/Desktop/07.AlertConfirmPromptDemo/AlertConfirmPromptDemo.html")

# alert弹窗
# b.find_element_by_xpath("//input[@onclick='myFunctionalert()']").click()
# alert_1 = b.switch_to_alert()
# print(alert_1.text)
# time.sleep(4)
# alert_1.accept()

# confirm
# b.find_element_by_xpath("//button[@onclick='myFunctionconfirm()']").click()
# alert_2 = b.switch_to_alert()
# print(alert_2.text)
# time.sleep(4)
# # 取消
# #alert_2.dismiss()
# # 确定
# alert_2.accept()

# prompt
b.find_element_by_xpath("//button[@onclick='myFunctionprompt()']").click()
alert_3 = b.switch_to_alert()
alert_3.send_keys("小明")
alert_3.accept()