import pymysql
conn = pymysql.connect(host='127.0.0.1', user='admin', password='123456', database='itProger')
cursor = conn.cursor()
cursor.execute('SELECT `id` FROM `shop`;')
row = cursor.fetchone()
while row:
    print(str(row))
    row = cursor.fetchone()

conn.close()
