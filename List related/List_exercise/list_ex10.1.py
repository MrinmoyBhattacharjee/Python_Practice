import string
#list=string.ascii_lowercase
list = 'abcdefghijklmnopqrstuvwxyz'
count=1
newList=[]
for i in list:
 newList.append(i*count)
 count+=1
print(newList)