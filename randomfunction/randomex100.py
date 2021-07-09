import random
def fun(n):
    if(n==2):
      x=random.randint(10,99)
    elif(n==3):
      x=random.randint(100,999)
    elif(n==4):
      x=random.randint(1000,9999)



    return x
#main
n=int(input("enter a numbrer="))
v=fun(n)
print(v)

