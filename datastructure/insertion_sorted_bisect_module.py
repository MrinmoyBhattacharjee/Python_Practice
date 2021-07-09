import bisect
n=int(input("Enter the desired linear list size="))
ar=[0]*n
print("Enter Elements for Linear List\n")
for i in range(n):
    ar[i]=int(input("Element"+str(i)+":"))
item=int(input("Enter the element to be insert ="))
ind=bisect.bisect(ar,item)  # bisect module only work with ascending order
bisect.insort(ar,item)
print(item,"inserted  at index",ind)
print("List after insertion\n")
for i in range(len(ar)):
    print(ar[i],end=" ")