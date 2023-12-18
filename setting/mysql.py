# 编码人：TFY
# 时间：2022/6/18
import pymysql

#mysql_info
lemon = {
    'host':'47.113.180.81',
    'user':'lemon',
    'password':'lemon123',
    'db':'yami_shops',
    'port':3306,
    'autocommit':True,
    'cursorclass':pymysql.cursors.DictCursor,
    'charset':'utf8'
}
