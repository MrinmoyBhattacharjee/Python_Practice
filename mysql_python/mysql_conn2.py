import mysql.connector as con
mycon=con.connect(host='localhost',user='root',passwd='root',database='world')
'''
a database cursor object can be created that gets the access of all the records
 retrieved as per query(called resultset) and allow us to traverse 
 the resultset row by row
'''
cursor=mycon.cursor()
#we can create a cursor object using cursor() function
#here cursor --> is a cursor object
# now we can execute sql query using execute function with cursor object
cursor.execute('select * from city')
#now data is stored at cursor object,we can extract data from the resultset
#using any of the following function:
'''
data=cursor.fetchall()
data=cursor.fetchone()
data=cursor.fetchmany(n)
variable=cursor.rowcount -> returns total no of row retrieved from the cursor

'''
