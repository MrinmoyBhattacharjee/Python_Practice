myList = [1, 2, 3, 4, 5]
print('List: ', myList)

myList=(myList[-1:] + myList[:-1])
print('After rotating: ', myList)
