#sum of list elements
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

l=[3,4,7,8,11]
print(sum(l))

l=eval(input("enter the list value="))
print(sum(l))