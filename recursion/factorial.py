def fact(n):
 if(n==0): #
    return 1
 else:
     v= n*fact(n-1)
     return v
#_main_
n=int(input("Enter a number="))
v=fact(n)
print(v)


