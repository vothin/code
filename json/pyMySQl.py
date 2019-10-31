import pymysql
import json


class JsonDataFile:

    def __init__(self):
        self.db = pymysql.connect(                  # connect()     链接数据库
                host = "39.108.248.223",
                port = 3306,
                user = "root",
                password = "qwe123",
                db = "wdkl_member")

        self.cur = self.db.cursor()                 # cursor()      设置数据库游标对象
        self.sql = ""                               # 建立sql语句
        self.selectData = ()                        # 获取数据
        self.tableDesc = ()                         # 获取表结构
        self.selectData_list = []                   # 获取数据列表
        self.tableDesc_list = []                    # 获取表结构列表
        self.selectData_dict = {}                   # 获取数据对应字典
        self.jsonData_dict = {}                     # 获取json文件

    def writeSqlStatement(self):

        # self.sql = input("输入SQL语句：")            # 编写SQL语句
        self.sql = "select * from es_member where mobile = '15502043438';"
        self.cur.execute(self.sql)                  # executr()     执行SQL语句
        self.selectData = self.cur.fetchone()       # fetchone()    获取数据
        # print(self.selectData)
        self.tableDesc = self.cur.description       # description() 获取表结构
        # print(self.tableDesc)

    def closeDatabases(self):
        self.cur.close()                            # 关闭数据库游标
        self.db.close()                             # 关闭数据库

    def getData(self):
        # for each in self.selectData:
        #     self.selectData_list.append(each)
        self.selectData_list = list(self.selectData)
        # print(self.selectData_list)

        for each in self.tableDesc:
            self.tableDesc_list.append(each[0])
        # print(self.tableDesc_list)

        for each in range(len(self.tableDesc_list) - 1):
            self.selectData_dict[self.tableDesc_list[each]] = self.selectData_list[each]
        # print(self.selectData_dict)

    def jsonDataDict(self):

        self.jsonData_dict = json.dumps(self.selectData_dict)
        return self.jsonData_dict




if __name__ == "__main__":
    j = JsonDataFile()
    j.writeSqlStatement()
    j.closeDatabases()
    j.getData()
    j.jsonDataDict()
    print(j.jsonData_dict)




            # msg = db
            # title = "数据库查询"

# db = pymysql.connect(
#     host = "39.108.248.223",
#     port = 3306,
#     user = "root",
#     password = "qwe123",
#     db = "wdkl_member")
#
# cursor = db.cursor()
#
# # cursor(设置数据库游标对象)
# cursor = db.cursor()
#
# # 查看多少数据库   execute(查询数据)
# databasesCount = cursor.execute("show databases;")
# # print(databasesCount )
#
# # 查看具体数据库   fetchall(查询所有数据库)
# showDatabases = cursor.fetchall()
# print(showDatabases)
# #
# # 查询表
# selectTable = cursor.execute("select * from es_member where mobile = '15502043438';")
# # print(selectTable)
#
# # 查询单条数据    fetchone(查询单条数据)
# selectData = cursor.fetchone()
# print(selectData)
#
# # print(cursor.description)
#
# tableDesc = cursor.description
# print(tableDesc)
#
# # 查询表字段
# data_list = []
# for each in tableDesc:
#     data_list.append(each[0])
# # print(data_list)
#
# # 查询表的值
# selectData_list = []
# for each in selectData:
#     selectData_list.append(each)
# print(selectData_list)
#
# selectData_dict = {}
# for i in range(len(data_list) - 1):
#
#     # selectData_dict = {}
#     selectData_dict[data_list[i]] = selectData_list[i]
#     #
#     # if i == (len(data_list) - 1):
#     #     selectData_dict = selectData_dict{}
#
# print(selectData_dict)
#
#
# json_dict = json.dumps(selectData_dict)
# print(json_dict)
