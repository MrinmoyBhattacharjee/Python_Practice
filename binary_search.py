def  bsearch( a,e):
    beg=0
    end=len(a)-1
    mv=(beg+end)//2
    while( beg<=end and a[mv]!=e):

      if(e<a[mv]):
        end=mv-1
      else:
       beg=mv+1
      mv=(beg+end)//2

    if(a[mv]==e):
         print("the elements is found at position=",mv+1)
    else:
        print("the elements is  not found ")
n=int(input("enter a number of element"))
l=[0]*n

for i in range(n):
    l[i]=int(input("element"+str(i)+":"))
s=int(input("Enter the searching element="))
bsearch(l,s)