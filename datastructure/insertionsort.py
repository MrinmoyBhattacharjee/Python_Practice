
l=eval(input("enter a list="))
n=len(l)
print("original list",l)
for i in range(1,n):
    k=l[i]
    j=i-1
    while(j>=0 and k<l[j]):
        l[j+1]=l[j]
        j=j-1
    else:
        l[j+1]=k
print("after sorting",l)

