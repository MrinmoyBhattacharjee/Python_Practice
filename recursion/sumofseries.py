def sumofseries(n):
 if(n==0):
    return 0
 else:
     return n+sumofseries(n-1)
#_main_
n=int(input("Enter a number="))
v=sumofseries(n)
print(v)
