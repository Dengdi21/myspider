# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class Num2MeijuPipeline(object):
    def process_item(self, item, spider):
        return item


class MeiJuPipeline(object):
    '''
    此方法必须被实现
    用来具体处理item内容
    '''

    def __init__(self):
        self.file = open('meiju.json', 'wb')

    def process_item(self, item, spider):
        '''
        此案例只是把item值打印出来
        :param item:
        :param spider:
        :return:
        '''
        with open('meiju.json', 'a') as f:
            json.dump(dict(item), f)
        return item