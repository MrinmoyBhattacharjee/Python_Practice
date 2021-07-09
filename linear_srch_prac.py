def lsearch(ar,a):
    l=len(ar)
    i=0
    while (i<l and ar[i]!=a):

      i+=1
    if(i<l):
       return i
    else:
         return False
#main
n=int(input("enter a number of element"))
l=[0]*n

for i in range(n):
    l[i]=int(input("element"+str(i)+":"))
a=int(input("enter a number to be searched"))

index=lsearch(l,a)
if index:
    print("element found at ",index+1)
else:
    print("not found")
