import string
listABCD=string.ascii_lowercase
print(listABCD)
count=1
l=[]
for i in listABCD:
 l.append(i*count)
 count+=1
print(l)