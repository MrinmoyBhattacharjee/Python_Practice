l=[]
n=int(input("enter the no.of values="))
for i in range(n):
    x=int(input("enter the value between 1 to 12="))
    if x>12:
        print("Out of range")
    else:
     l.append(x)
print("First List=",l)
m=len(l)
for i in range(m):
    if l[i]>10:
       l[i]=10
print(l)
