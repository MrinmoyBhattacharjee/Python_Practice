l=eval(input("enter a list="))
n=len(l)
for i in range(0,n):
 for j in range(i+1,n):
  if(l[i]>l[j]):
          t=l[i]
          l[i] = l[j]
          l[j]=t
print("list after sorting=")
print(l)
