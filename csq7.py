import random

def func(n):
  if(n==2):

    x=random.randint(10,99)
  elif(n==3):
    x = random.randint(100, 999)
  elif (n == 4):
      x = random.randint(1000, 9999)
  return x
n=int(input("Enter the value of n="))



v=func(n)
print(" ", v)