fileobj=open("Record4.txt","w")
n=int(input("Enter the total no of records="))
list=[]
for i in range(n):
    roll=input("Enter Roll No=")
    list.append(roll)
    name=input("Enter the name=")
    list.append(name)
    marks=input("Enter Marks=")
    list.append(marks+'\n')

fileobj.writelines(list)

fileobj.close()