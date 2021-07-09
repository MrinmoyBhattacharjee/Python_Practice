from random import randint

def randomNumber(n):
    x = int('9'*(n-1))+1 # first n-digit number, string is converted back to int
    y = int('9'*n) # last n-digit number
    return randint(x, y)

n = int(input('Enter a number :'))
print(randomNumber(n))