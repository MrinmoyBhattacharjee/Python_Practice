#wap to count no of even pairs in a given tuple
NTuple = ((2, 5), (4, 2), (9, 8), (12, 10))
c = 1
for i, j in NTuple:
    if (i % 2 == 0) and (j % 2 == 0):
        print(i, j)
        c = c+ 1
print('So the number of even pairs in NewTuple are : ', c)

