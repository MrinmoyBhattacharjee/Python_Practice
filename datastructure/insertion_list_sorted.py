def insert_sorted(ar,item):
 ar.append(0)
 i = len(ar)-2
 while(item<ar[i]):
        ar[i+1] = ar[i]
        i-=1
 ar[i + 1] = item
#_main_
n=int(input("Enter the desired linear list size="))
ar=[0]*n
print("Enter Elements for Linear List\n")
for i in range(n):
    ar[i]=int(input("Element"+str(i)+":"))
item=int(input("Enter the element to be insert ="))
insert_sorted(ar,item)
print("List after insertion\n")
for i in range(len(ar)):
    print(ar[i],end=" ")

