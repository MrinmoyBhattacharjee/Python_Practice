def binary_search(a,s,beg,end):
    if(beg>end):
        return -1

    mid=(beg+end)//2
    if (a[mid] == s):
        return mid
    elif(s < a[mid]):
      end=mid-1
      return binary_search(a,s,beg,end)
    elif(s>a[mid]):
     beg=mid+1
     return binary_search(a, s, beg, end)
#_main_
a=[12,14,15,18,21,34,37]
beg=0
end=len(a)-1

s=int(input("Enter the searching element="))
l=binary_search(a,s,beg,end)
if l>=0:
    print(s,"found at location",l+1)
else:
    print(s,"not found")



