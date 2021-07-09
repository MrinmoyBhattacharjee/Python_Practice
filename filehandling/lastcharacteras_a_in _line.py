f=open("abc.txt","r")
c =0
linelist=f.readlines()
print(linelist)
for line in linelist:
 if line[-2] == 'a':
   c=c+1
print("Number of lines having 'a' as last character is/are : " ,c)
f.close()