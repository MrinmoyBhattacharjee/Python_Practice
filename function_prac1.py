n=int(input("Enter a number="))
r=int(input("Enter a number="))
f1=1
f2=1
f3=1
for i in range (1,n+1):
        f1=f1*i
for i in range (1,r+1):
        f2=f2*i
for i in range (1,n-r+1):
        f3=f3*i
v=f1/(f2*f3)
print(v)

