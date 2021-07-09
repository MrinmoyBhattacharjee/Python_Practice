#Write a function that takes a number and tests if
# it is a prime number using recursion technique.
def primeOrNot(num, n):
    if n >= 2:
        if (num % n) == 0:
            return False
        else:
            return primeOrNot(number, n - 1)
    elif num == 1:
        return False
    else:
        return True
number =int(input("Enter a number: "))
if primeOrNot(number, number - 1):
    print("The number is a prime number")
else:
    print("The number is not a prime number")