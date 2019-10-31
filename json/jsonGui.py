import pyMySQl
import easygui as g
import os

# msg1 = "欢迎使用自制mysql转json文件程序" \
#        "制作人：某蹩脚程序员"
# msg2 = "输入搜索语句"
# title = "mysql转json文件"

class easyGui:
    def __init__(self):
        self.msg1 = "欢迎使用自制mysql转json文件程序" \
                    "制作人：某蹩脚程序员" \
                    "这是付费程序！！！"
        self.msg2 = "输入搜索语句"
        self.msg3 = "搜索结果为："
        self.title = "mysql转json文件"
        self.sql = ""
        self.text = ""
        self.sql = ""

    def msgBox(self):
        g.msgbox(self.msg1, self.title, ok_button = "30￥")


    def enterBox(self):
        g.enterbox(self.msg2, self.title)
        return self.sql

    def textBox(self):
        g.textbox(self.msg3, self.title, self.text)


e = easyGui()
m = pyMySQl.JsonDataFile()
e.msgBox()


e_sql = e.enterBox()
m.writeSqlStatement()
m.sql = e_sql
m.closeDatabases()
m.getData()
m.jsonDataDict()

with open(r"C:\Users\zhangyi\Desktop\json.txt", "w", encoding = "utf-8") as f:
    f.write(m.jsonData_dict)
    f.close()

with open(r"C:\Users\zhangyi\Desktop\json.txt", "r", encoding = "utf-8") as f:
    json_msg = os.path.basename(r"C:\Users\zhangyi\Desktop\json.txt")
    msg = "文件【%s】的内容如下：" % json_msg
    text = f.read()
    g.textbox(msg, e.title, text)

# select * from es_member where mobile = '15502043438';

