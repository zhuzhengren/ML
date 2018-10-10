import pymysql
import Config

conn = pymysql.connect(**Config.sql_conn_dict)
cur=conn.cursor()

sql = 'select * from student'
cur.execute(sql)
#cur.fetchone()
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())




cur.close()
conn.close()


