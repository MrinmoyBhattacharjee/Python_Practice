def insertion(ar,item):
    ar.append(0)
    i=len(ar)-2
    while(item<ar[i]):
        ar[i+1]=ar[i]
        i=i-1
    ar[i+1]=item

#main
n=int(input("enter a number of element"))
ar=[0]*n
for i in range(n):
    ar[i]=int(input("enter"+str(i)+":"))
a=int(input("enter a number to be insert "))
insertion(ar,a)
for i in range(len(ar)):
    print(ar[i],end=" ")

