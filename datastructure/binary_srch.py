def BSearch(ar,item):
    beg=0
    end=len(ar)-1
    while(beg<end):
        mid = (beg + end) // 2
        if(item==ar[mid]):
            return mid
        elif (item>ar[mid]):
            beg=mid+1
        else:
            end=mid-1
    else:
        return False
#main
n=int(input("Enter the desired linear list size="))
ar=[0]*n
print("Enter Elements for Linear List\n")
for i in range(n):
    ar[i]=int(input("Element"+str(i)+":"))
item=int(input("Enter the element to search for="))
index=BSearch(ar,item)
if index:
    print("\n Element found at index:",index,"Location=",(index+1))
else:
    print("\n Element not found")
