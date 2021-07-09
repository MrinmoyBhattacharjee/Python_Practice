def BSearch(ar,item,beg,end):
    if beg>end:
      return -1

    mid = (beg + end) // 2
    if (item == ar[mid]):
        return mid
    elif (item < ar[mid]):
        end = mid - 1
        return BSearch(ar,item,beg,end)

    elif item > ar[mid]:
        beg = mid +1
        return BSearch(ar, item, beg, end)

ar=[12,17,19,22,25,28]
item=int(input("Enter the element to search for="))
index=BSearch(ar,item,0,len(ar)-1)
if index >=0:
    print("\n Element found at index:",index,"Location=",(index+1))
else:
    print("\n Element not found")