def fact(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    return f
n=int(input("Enter a value of n="))
r=int(input("Enter a value of r="))
v=fact(n)/(fact(r)*fact(n-r))
print("Value of ncr =",v)