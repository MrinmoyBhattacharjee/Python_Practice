import random
str="CBSEONLINE"
number=random.randint(0,3)
n=9
while str[n]!='L':
    print(str[n]+str[number]+'#',end='')
    number=number+1
    n=n-1
