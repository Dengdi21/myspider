from pymongo import MongoClient


class MongoAPI(object):
    def __init__(self, db_ip, db_port, db_name, table_name):
        self.db_ip = db_ip
        self.db_port = db_port
        self.db_name = db_name
        self.table_name = table_name
        self.conp = MongoClient(host=self.db_ip, port=self.db_port)

        self.db = self.conp[self.db_name]

    # 获取一条数据
    def get_one(self, query):
        return self.table.find_one(query, property={"_id": False})

    # 获取多条数据
    def get_all(self, query):
        return self.table.find(query)

    # 添加数据
    def add(self, kv_dict):
        return self.table.insert(kv_dict)

    # 删除数据
    def delete(self, query):
        return self.table.delete_many(query)

    # 查询数据
    def check(self, query):
        ret = self.table_name.find_one(query)
        return ret != None

    def update(self, query, kv_dict):
        self.table.update_one(query, {'$set': kv_dict})