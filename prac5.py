import math

a=int(input("enter a number= "))
b=int(input("enter a number= "))
c=int(input("enter a number= "))
d=(b**2)-(4*a*c)
if(d>0):
    print("distinct root=",(-b+math.sqrt(d))/(2*a),(-b-d**1/2)/(2*a))
elif(d==0):
    print("equal roots=",-b/(2*a),-b/(2*a))
else:
    print("imaginary roots")