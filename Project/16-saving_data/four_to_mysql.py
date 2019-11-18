"""
数据存储之mysql

登录数据库：
#sudo mysql -u 用户 -p
#密码：。。。。。。

mysql 远程联通：
1.修改/etc/mysql/my.cong
    注释bind-address = 127.0.0.1
    或者修改为bind-address = 0.0.0.0
2.让root用户支持远程连接
    mysql -u root -p
    grant all privileges on *.* to root@'%' identified by "yourpassword" with grant option;
    flush privileges
3.rhe17中防火墙允许mysql服务通过
    firewall-cmd --permanent --add-service=mysql
    firewall-cmd --reload


在python中操作mysql
1.安装pymysql
    pip install pymysql

"""

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


# 其他增删改查均可以使用类似代码块







