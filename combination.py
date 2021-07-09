def comb(x):
    f1=1

    for i in range(1,x+1):
        f1=f1*i
    return f1
n=int(input("Enter a number="))
r=int(input("Enter a number="))
c=comb(n)/(comb(r)*comb(n-r))
print("combination=",c)
