l=[]
n=int(input("enter the no.of values"))
for i in range(n):
 x=int(input("enter the value"))
 l.append(x)
print("Original List=",l)
print("Sum of all elements=",sum(l))
l.reverse()
print("Reverse List=",l)

