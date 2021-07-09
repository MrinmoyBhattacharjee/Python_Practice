fileobj=open("Record2.txt","w")
n=int(input("Enter the total no of records="))
for i in range(n):
    roll=input("Enter Roll No=")
    name=input("Enter the name=")
    marks=input("Enter Marks=")
    rec=roll+" "+name+marks+'\n'
    fileobj.write(rec)

fileobj.close()