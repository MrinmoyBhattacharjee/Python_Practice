s="www.google.com"
c=0
print(s.strip('w'))
s1=list(s)
#print(s1)
for i in s1:
    if i=='w':
        c=c+1
print(c)