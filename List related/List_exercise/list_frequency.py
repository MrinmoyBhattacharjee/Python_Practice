'''l=[]

n=int(input("Enter the no of values to be input="))
print("enter",str(n),"  values")
for i in range(n):
    x=int(input("Enter the value="))
    l.append(x)
print("Original List",l)'''

l=eval(input("enter the list"))
x=input("enter the element to be found")
L=len(l)
c=0
for i in range(L):
    if(l[i]==x):
        c=c+1
print(c)
