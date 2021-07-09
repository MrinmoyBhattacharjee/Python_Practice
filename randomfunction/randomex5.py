import random
pick=random.randint(0,3)
#print(pick)
city=["Delhi","Mumbai","Chennai","Kolkata"]
for i in city:
    for j in range(1,pick):
        print(i,end='')
    print()

