def insert_unsorted(ar,item,loc):
 ar.append(0)
 i = len(ar)-2
 while(i>=loc-1):

        ar[i+1] = ar[i]
        i-=1
 ar[loc-1] = item
#_main_
n=int(input("Enter the desired linear list size="))
ar=[0]*n
print("Enter Elements for Linear List\n")
for i in range(n):
    ar[i]=int(input("Element"+str(i)+":"))
item=int(input("Enter the element to be insert ="))
loc=int(input("Enter the location to be insert ="))
insert_unsorted(ar,item,loc)
print("List after insertion\n")
for i in range(len(ar)):
    print(ar[i],end=" ")

