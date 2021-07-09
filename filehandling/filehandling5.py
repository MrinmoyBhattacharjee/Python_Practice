# write  user given data into input file using write() function

fileobj=open("Record.txt","w")
n=int(input("Enter the total no of records="))
for i in range(n):
    name=input("Enter the name=")
    fileobj.write(name)
    fileobj.write("\n")
fileobj.close()