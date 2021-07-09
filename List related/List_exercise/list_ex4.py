l=[]
n=int(input("enter the no. of values"))
for i in range(n):
    x=int(input("enter the value"))
    l.append(x)
print("list 1=",l)
m=[]

for i in range(n):
    y=int(input("enter the value"))
    m.append(y)
print("list 2=",m)
a=[]
for i in range(n) :
    a.append(l[i]+m[i])

print(a)

