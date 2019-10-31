from day8.Config.EcshopConf import *
import pymysql


class mysql_operation(object):
    # 打开数据库连接
    # db 第一个：IP地址，数据库用户名，数据库密码，数据库名，端口--默认3306
    def __init__(self):

        self.db = pymysql.connect(sit_db_server, sit_db_user, sit_db_password, sit_db_name)

        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

    def mysql_add(self):
        pass

    def mysql_select(self):
        pass

    def mysql_update(self):
        pass

    def mysql_inserinto(self):
        # 使用 execute()  方法执行 SQL 查询
        # cursor.execute("SELECT VERSION()")
        self.cursor.execute("SELECT * FROM EMPLOYEE WHERE INCOME > 1000")

        # 使用 fetchone() 方法获取单条数据.
        data = self.cursor.fetchall()

        print("Database version : ", data, type(data))
    def mysql_user_select(self):
        pass

    # 关闭数据库连接
    # self.db.close()
