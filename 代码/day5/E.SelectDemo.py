from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

b = webdriver.Chrome()
b.get("http://192.168.3.246/ecshop/user.php?act=register")

# 二次定位
# b.find_element_by_name("sel_question").find_element_by_xpath("//option[@value='interest']").click()
# sleep(3)
# b.find_element_by_name("sel_question").send_keys("我最喜爱")

select_1 = Select(b.find_element_by_name("sel_question"))

# select_1.select_by_index(3)                       #主下标来选择下拉列表
# sleep(3)
# select_1.select_by_value("favorite_equipe")       #下拉列表的value来选择
# sleep(3)
# select_1.select_by_visible_text("我最喜欢的小说？")  #使用文本来选择下拉菜单的选项

# 01 options 列出所有的下拉值
# for i in select_1.options:
#     print(i.text)
#
# # 02 默认的值选项
select_1.select_by_index(3)                       #主下标来选择下拉列表
sleep(3)
select_1.select_by_value("favorite_equipe")       #下拉列表的value来选择
sleep(3)
select_1.select_by_visible_text("我最喜欢的小说？")  #使用文本来选择下拉菜单的选项
# options1 = select_1.all_selected_options
for j in select_1.all_selected_options:

    print("当前多选中的默认项：", j.text)
#
# # 03 当前选项的文本
print("当前的选项", select_1.first_selected_option.text)


'''
总结

select_by_index(index) ——通过选项的顺序，第一个为 0 
select_by_value(value) ——通过value属性 
select_by_visible_text(text) ——通过选项可见文本

options ——提供所有的选项的列表，其中都是选项的WebElement元素 
all_selected_options ——提供所有被选中的选项的列表，其中也均为选项的WebElement元素 
first_selected_option ——提供第一个被选中的选项，也是下拉框的默认值


deselect_by_index()     ：取消对应index选项
deselect_by_value()      ：取消对应value选项
deselect_by_visible_text() ：取消对应文本选项
deselect_all()          ：取消所有选项

前三种分别于select相对应，第四种是全部取消选择，是的，你没看错，是全部取消。有一种特殊的select标签，
即设置了multiple=”multiple”属性的select，这种select框是可以多选的，你可以通过多次select，
选择多项选项，而通过deselect_all()来将他们全部取消。
'''