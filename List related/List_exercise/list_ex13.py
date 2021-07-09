'''
 Start with the list [8,9,10]. Do the following:
(a) Set the second entry (index 1) to 17
(b) Add 4, 5, and 6 to the end of the list
(c) Remove the first entry from the list
(d) Sort the list
(e) Double the list
(f) Insert 25 at index 3
The final list should equal [4,5,6,25,10,17,4,5,6,10,17]
'''
l=[8,9,10]
# (a) Set the second entry(index 1) to 17
l[1]=17
# (b) Add 4,5, and 6 to the end of the list
l.append(4)
l.append(5)
l.append(6)
# (c) Remove the first entry from the list
del l[0]
# (d) Sort the list
l.sort()
# (e) Double the list
l=l*2
# (f) Insert 25 at index 3
l.insert(3,25)
# Final List
print('Final List :',l)