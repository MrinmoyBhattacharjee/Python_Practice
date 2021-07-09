import mysql.connector as con
# To create a connection with mysql
# connect() function establish  a connection to mysql and required four parameter
# specify a python identifier(variable) as connection object name
mycon=con.connect(host='localhost',user='root',passwd='root',database='world')
#connection_object=connection_alias.connect(host,user,passwd,database)
if mycon.is_connected():
    print("database connection established")

