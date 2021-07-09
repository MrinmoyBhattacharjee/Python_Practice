def Fn(n):
    print(n,end=" ")
    if(n<3):
        return n
    else:
        return Fn(n//2)-Fn(n//3)
Fn(12)
#print("")
#Fn(10)
#print("")
#Fn(7)