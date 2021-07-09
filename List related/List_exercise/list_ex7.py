#Ask the user to enter a list of strings. Create a new list that consists
# of those strings with their first characters removed.

l=[]
n = int(input('Enter the number of string : '))

for i in range(n):
    s = input('Enter the string : ')
    l.append(s)

print(l)

d=[]
#
for item in l:

    n = item[1:len(item)]
    d.append(n)


print(d)
