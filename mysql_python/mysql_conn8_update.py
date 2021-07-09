import mysql.connector as con
mycon=con.connect(host='localhost',user='root',passwd='root',database='test')
cursor=mycon.cursor()
st="update info set marks={} where  name='{}'".format(90,'ram')
cursor.execute(st)
mycon.commit()