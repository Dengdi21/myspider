"""
python链接mysqldemo

1.获取数据库 pymaql Mysqldb
2.获取记录
3.增加记录
4.修改记录
5.删除目录

"""

__author__ = 'chumu'
__time__ = '2019.11'

import pymysql


class MysqlDemo(object):
    # 设置数据库的链接参数，默认编码为utf-8
    def __init__(self, host, username, password, dbname):
        self.conn = pymysql.connect(host, username, password, dbname, charset='utf-8')
        self.cursor = self.conn.cursor()

    def get_all(self, sql):
        """
        获取全部数据
        :param sql:
        :return:
        """
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            return False

    def get_one(self, sql):
        """
        获取一条数据
        :param sql:
        :return:
        """
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            return results
        except Exception as e:
            print(e)
            return False

    def insert(self, table_name, data):
        """
        插入数据
        :param table_name:
        :param data:
        :return:插入后的id
        """
        if len(data.keys()) == 1:
            sql = 'insert into {}({}) value '.format(table_name, data.keys[0]).replace("'", '') + '({})'.format(data.values)
        else:
            sql = 'insert into {}({}) value '.format(table_name, data.keys).replace("'", '') + str('({})'.format(tuple(data.values)))

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return int(self.cursor.lastrowid)
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False

    def query(self, sql):
        """
        执行一条sql语句
        :param sql:
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return int(self.cursor.lastrowid)
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False


    def update(self, table_name, data, restrication_str):
        """
        更新记录
        :param table_name: 表明
        :param data: 字典
        :return: str
        """
        data_str = ''
        for item in data.items():
            data_str += '{}="{}",'.format(item[0], item[1])

        values =  data_str[:-1]
        sql = 'update {} set {} where {}'.format(table_name, data_str, restrication_str)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)

    def delete(self):
        """
        删除一条数据
        :return:
        """
        sql = ''
        pass

    def delete_table(self, table_name):
        """
        删除表
        :param table_name:
        :return:
        """
        sql = ''
        pass

    def format_tab(self, table_name):
        """
        格式化表
        :param table_name:
        :return:
        """
        sql = 'trncate table {}'.format(table_name)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)



















