l=[]
r=int(input("Enter the no of rows="))
c=int(input("Enter the no of columns="))
for i in range(r):
    row=[]
    for j in range(c):
        e=int(input("Enter the element of "+str(i)+str(j)+":"))
        row.append(e)
    l.append(row)
print(l)

for i in range(r):

    for j in range(c):
        print(l[i][j],end=" ")
    print("")