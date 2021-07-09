def gcdcalculate(a, b):
    if (b == 0):
        return a
    else:
        return gcdcalculate(b, a % b)


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("The gcd of ",a ,"and ",b," is =: ",gcdcalculate(a,b), end="")
