def express(x,n):
    if n==0:
        return 1
    elif n%2==0:
        return express(x*x,n/2)
    else:
        return x*express(x,n-1)
v=express(2,5)
print(v)