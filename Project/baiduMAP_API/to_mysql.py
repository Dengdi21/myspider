import pymysql


# 操作数据库
try:
    # 获取一个数据库连接：
    # 打开一个数据库连接：
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='12345678', db='ceshi', port=3306)
    # 创建游标
    cursor = db.cursor()
    # 使用excute()执行sql语句
    cursor.execute('DROOP TABLES IF EXISTS BJTLXY')
    # 创建表
    sql ="create table BJTLXY(FIRST_NAME CHAR(20) NOT NULL,LAST_NAME CHAR(20),AGE INT,SEX  CHAR(1),INCOME FLOAT)"
    cursor.execute(sql)
    db.close()
except:
    print('创建失败')
