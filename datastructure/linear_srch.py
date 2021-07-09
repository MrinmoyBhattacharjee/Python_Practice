def LSearch(ar,item):
    l=len(ar)
    i=0
    while(i<l and ar[i]!=item):
        i+=1
    if(i<l):
        return i
    else:
        return False
#main
n=int(input("Enter the desired linear list size="))
ar=[0]*n
print("Enter Elements for Linear List\n")
for i in range(n):
    ar[i]=int(input("Element"+str(i)+":"))
item=int(input("Enter the element to search for="))
index=LSearch(ar,item)
if index:
    print("\n Element found at index:",index,"Location=",(index+1))
else:
    print("\n Element not found")
