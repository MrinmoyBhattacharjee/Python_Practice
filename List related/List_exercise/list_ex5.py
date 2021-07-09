l=[]
ch=97
for i in range(26):
 for j in range(i+1):
  l.append(chr(ch))
 ch=ch+1
print(l)