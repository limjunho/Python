import pymysql

### Database connect ###
conn = pymysql.connect(host='127.0.0.1', user='test', password='george7790',
        db='test_db', charset='utf8')
### get Cursor ###
curs = conn.cursor()
### insert CONST_COMMAND ###
sql = """insert into test_table(number, data1, data2, data3) values(%s, %s, %s, %s)"""

curs.execute(sql, (3, 'g', 'h', 'i'))

conn.commit()

conn.close()
