l=[]
f=0
n=int(input("Enter the no of values to be input="))
print("enter",str(n),"  values")
for i in range(n):
    x=int(input("Enter the value="))
    l.append(x)
m=int(input("enter the element to be found="))
for i in range(n):
    if l[i]==m:
        f=1
if f==1:
  print("Item found")
else:
 print("Item not found")