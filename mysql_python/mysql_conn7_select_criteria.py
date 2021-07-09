import mysql.connector as con
mycon=con.connect(host='localhost',user='root',passwd='root',database='test')
cursor=mycon.cursor()
st="select * from info where marks={} and name='{}'".format(70,'ram')
cursor.execute(st)
data=cursor.fetchall()
for row in data:
    print(row)
    '''print("Roll No=",row[0])
    print("Name=", row[1])
    print("Marks=", row[2])
    print("Phone Number=", row[3])'''