def atothepowern(a,n):
 if(n==0):
    return 1
 else:
     return a*atothepowern(a,n-1)
#_main_
a=int(input("Enter the value of a="))
n=int(input("Enter the value of n="))
v=atothepowern(a,n)
print(v)
