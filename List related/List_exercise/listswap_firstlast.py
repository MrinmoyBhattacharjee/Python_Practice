l=[]

n=int(input("Enter the no of values to be input="))
print("enter",str(n),"  values")
for i in range(n):
    x=int(input("Enter the value="))
    l.append(x)
print("Original List",l)
l[0],l[-1]=l[-1],l[0]
print(l)