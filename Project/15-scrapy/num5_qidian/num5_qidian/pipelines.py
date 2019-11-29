# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Num5QidianPipeline(object):
    def process_item(self, item, spider):
        return item


import pymysql

class MYqidianSQL(object):
    def __init__(self):
        # (ip, 用户， 密码，数据库， 字符集)
        self.conn = pymysql.connect('127.0.0.1', 'root', '12345678')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        pass

    def close_spider(self):
        self.cursor.close()
        self.conn.close()

class MyQiDiqnPipeline(MYqidianSQL):
    def process_item(self, item, spider):
        sql = 'insert into qidianreader VALUES (null,%s,%s,%s,%s)'
        data = (item['titel'], item['href'], item['author'], item['info'])

        try:
            self.cursor.execute(sql, data)
            self.conn.commit()
        except Exception as e:
            print('插入失败')
            print(e)