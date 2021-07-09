l=[]
n=int(input("Enter the no of values to be input="))
print("enter",str(n),"  values")
for i in range(n):
    x=int(input("Enter the value="))
    l.append(x)
eve=[]
odd=[]
for i in range(n):
    if l[i]%2==0:
        eve.append(l[i])
    else:
        odd.append(l[i])
print("Full List=",l)
print("Even List=",eve)
print("Odd List=",odd)