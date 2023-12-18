# 编码人：TFY
# 时间：2022/6/18

import pymysql

from setting.mysql import lemon


class HandleMySql:

    def __init__(self):
        # 创建链接
        self.connect = pymysql.connect(**lemon)
        # 创建游标
        self.cur = self.connect.cursor()

    # 获取数据库数据
    def get_data(self, str_sql):
        self.cur.execute(str_sql)
        return self.cur.fetchall()

    # 关闭数据库
    def close_mysql(self):
        self.cur.close()
        self.connect.close()



# if __name__ == '__main__':
#     print(type(my_sql.get_data("SELECT user_name FROM tz_user WHERE user_mobile = '17261557883' ")))
#     my_sql.close_mysql()


