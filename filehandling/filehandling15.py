f=open("abc.txt")
c=0
for line in f:
    if(line[0]=='T'):
     c=c+1
     print(line)

print("No of Lines start with T=",c)
f.close()