'''
2. Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list.
'''
from random import randint
l=[]
for i in range(20):
    r = randint(1,100)
    l.append(r)
# (a) Print the list.

print('List : ',l)
# (b) Print the average of the elements in the list.
print('Avegae :',sum(l)/len(l))
# (c) Print the largest and smallest value in the list.
print('Largest :',max(l),'  Smallest :',min(l))

# (d) Print the second largest and second smallest entries in the list.
c = l[:]
fmax=max(c)
fmin=min(c)
for i in range(len(c)-1):
    if c[i]==fmax:
        del c[i]
    if c[i]==fmin:
        del c[i]
print('Second Largest :',max(c),'  Second Smallest :',min(c));
# (e) Print how many even numbers are in the list.
c=0
for item in l:
    if item%2==0:
        c+=1
print('Count of even numbers :',c)