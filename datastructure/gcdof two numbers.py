def gcdcalculate(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("The gcd of ", a, "and ", b, " is =: ", gcdcalculate(a, b))