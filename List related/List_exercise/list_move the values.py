l=[]
n=int(input("enter the no. of values"))
for i in range(n):
    x=int(input("enter the value"))
    l.append(x)
print("list 1=",l)
v=l[-1]
for i in range(n-1,0,-1):
    l[i]=l[i-1]
l[0]=v

print(l)