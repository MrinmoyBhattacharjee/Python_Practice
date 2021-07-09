l=[]
n=int(input("enter the no. of values"))
for i in range(n):
    x=int(input("enter the value"))
    l.append(x)
print("original list=",l)
l.sort()
print("Second largest value=",l[-2])