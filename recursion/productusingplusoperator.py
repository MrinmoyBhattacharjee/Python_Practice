#Implement a function product() to multiply 2 numbers
# recursively using + and - operators only.
def product(x, y):
    # if x is less than y swap the numbers
   # if x < y:
       # return product(y, x)

        # iteratively calculate y times sum of x
    if y != 0:
        return (x + product(x, y - 1))
        # if any of the two numbers is zero return zero
    else:
        return 0

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
print(product(x, y))