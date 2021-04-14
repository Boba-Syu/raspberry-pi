from datetime import datetime

import pymysql


class MysqlLink:
    def __init__(self):
        self.db = pymysql.connect(host='81.68.230.143',
                                  user='root',
                                  password='hn123456Aa.',
                                  port=3306,
                                  database='cages',
                                  charset='utf8')

    def insert_temp(self, temperature):
        cursor = self.db.cursor()
        now = datetime.now()
        sql = "insert into temperature(id, temperature, create_time) VALUES (default ,'{}','{}')".format(temperature, now)
        print(sql)
        try:
            cursor.execute(sql)
            a = self.db.commit()
        except:
            print('error')
            self.db.rollback()
        cursor.close()


if __name__ == '__main__':
    mysql = MysqlLink()
    mysql.insert_temp(20.0)
