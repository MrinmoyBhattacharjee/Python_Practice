import mysql.connector as con
mycon=con.connect(host='localhost',user='root',passwd='root',database='test')
cursor=mycon.cursor()
st="insert into info(id,name,marks,phno) values({},'{}',{},{})".format(2,'shyam',80,9435554742)
cursor.execute(st)
mycon.commit()


