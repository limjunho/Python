import pymysql

### Database connect ###
conn = pymysql.connect(host='127.0.0.1', user='test', password='george7790',
        db='test_db', charset='utf8')
### get Cursor ###
curs = conn.cursor(pymysql.cursors.DictCursor)
### select CONST_COMMAND ###
sql = """select * from test_table"""

curs.execute(sql)

# fetchone() - 한번 호출에 하나의 Row를 가져올 때 사용
# fetchall() - 모든 데이터를 한꺼번에 가져올 때 사용
# fetchmany(n) - n개 만큼의 데이터를 가져올 때 사용

data = curs.fetchone()
print(data)

conn.close()
