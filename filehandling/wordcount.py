f=open("abc.txt","r")
linesList=f.readlines()
c=0
for line in linesList:
 wordsList=line.split()
 print(wordsList)
 c= c+ len(wordsList)
print("The number of words in this file are : ",c)
f.close()