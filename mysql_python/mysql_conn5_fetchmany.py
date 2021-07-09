import mysql.connector as con
mycon=con.connect(host='localhost',user='root',passwd='root',database='world')
cursor=mycon.cursor()
cursor.execute('select * from city')
data=cursor.fetchmany(4)
print(data)
c=cursor.rowcount
print(c)