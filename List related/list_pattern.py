
listABCD='abcdefghijklmnopqrstuvwxyz'

c=1
l=[]
for i in listABCD:
 l.append(i*c)
 c=c+1
print(l)