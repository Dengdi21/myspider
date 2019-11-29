# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class Num7LianjiaPipeline(object):
    def process_item(self, item, spider):
        return item


class MYLianjiaPipeline(object):
    def __init__(self):
        self.file = open('lianjia.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        str = json.dumps(dict(item), ensure_ascii=False)
        str = str + '\n'
        self.file.write(str)
        return item

    def close_spider(self):
        self.file.close()