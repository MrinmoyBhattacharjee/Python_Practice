#Ask the user to enter a list containing numbers between 1 and 12.
# Then replace all of the entries in the list that are greater than 10 with 10.

l=eval(input('Enter a list of number containing a number between 1-12 : '))
print('Before replacement : ',l)

for i in range(len(l)):
    if l[i]>10:
        l[i]=10

print('After replacement : ',l)