import random

def func(a,b):
    x=random.randint(a,b)
    return x
#main
p=int(input("Enter the starting point="))
q=int(input("Enter the ending point="))

print(" 3 Random numbers between the range=\n")
for i in range(3):
    v=func(p,q)
    print(" ",v)
