def one(x,y):
    if((x%10)>(y%10)) :
        return y

    else:
        return x


#main
x=int(input("enter a number="))
y=int(input("enter a number="))
print(one(x,y))