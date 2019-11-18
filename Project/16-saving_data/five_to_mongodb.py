"""
非关系型数据库
mongoDB属于更加适合爬虫的数据库
mongoDB是一个基于分布式文件存储的数据库，有c++编写
主要为web应用提供可拓展的高性能的数据存储解决方案

概念说明：
sql：      MongoDB：     说明：
database   database     数据库
table      collection   表/集合
row        document     行/文档
colume     field        字段/域管理
primary    primary      主键/_id为主键
"""


"""
安装MongoDB
    Ubuntu下安装（百度）
如何python操作MongoDB
    安装：pip install pymongo
    
"""
# 导入安装包
import pymongo

# 连接monggod
# client = pymongo.MongoClient()

# or
client = pymongo.MongoClient('127.0.0.1', 27017)

# or
# client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

# 获取到数据库，连接数据库
