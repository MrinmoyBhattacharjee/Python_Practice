l=[0,1]
n=int(input("enter the no. of values"))
for i in range(2,n):
    l.append(l[i-1]+l[i-2])
print("Fibonacci Series=",l)

'''

'''