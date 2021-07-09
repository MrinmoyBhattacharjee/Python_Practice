f=(0,)
n=int(input('Please enter a number= '))
a,b=0,1
for i in range(n-1):
 a,b = b,a+b
 f=f+(a,)
print(f)
rInput=int(input("Enter a fibonacci term: "))
print(f.index(rInput)+1)