L=[]
n=int(input("Enter the no of values to be input="))
print("enter",str(n),"  values")
for i in range(n):
    x=int(input("Enter the value="))
    L.append(x)
m=L[0]
for i in range(1,n):
    if L[i]>m:
        m=L[i]

print("Lagest value=",m)
print("#####Minimum Value####")
v=L[0]
for i in range(1,n):
    if L[i]<v:
        v=L[i]

print("Smallest value=",v)