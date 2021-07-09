import mysql.connector as con
mycon=con.connect(host='localhost',user='root',passwd='root',database='world')
cursor=mycon.cursor()
cursor.execute('select * from city')
data=cursor.fetchone()
print(data)
data=cursor.fetchone()
print(data)
c=cursor.rowcount
print("Row Count=",c)