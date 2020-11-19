#coding=utf-8
import pymysql.cursors

class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host='192.168.5.241',  # 数据库地址
            port=3306,  # 端口号
            user='root',  # 用户名
            passwd='zprd',  # 密码
            db='eplat_sit',  # 245数据库名称,246为eplat
            charset='utf8',  # 编码格式
            cursorclass=pymysql.cursors.DictCursor  # 获取数据库字段名

        )
        self.cur = self.conn.cursor() #创建游标

    def search_one(self,sql):
        self.cur.execute(sql) #execute执行sql语句
        result = str(self.cur.fetchone())
        return result


if __name__ == '__main__':
    op_mysql = OperationMysql()
    res = op_mysql.search_one("SELECT id,brand FROM `t_machine` WHERE creat_uid = '10099' and equip_is_online = '2'")
    print(res)
    print(type(res))
