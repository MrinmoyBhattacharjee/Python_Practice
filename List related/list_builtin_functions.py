l=[7,8,9,11,23]
#list index function
print(l.index(23))
#List extend function
m=[100,200]
l.extend(m)  #list.extend(value)
print(l)
#insert function  list.insert(pos,value)
m.insert(2,300)

#using append function ,we can add value to the list at end position
l.append(12)
print(l)
#pop method use delete to  list.pop() -this delete last value
#list.pop(pos)  -this delete from the given postion
print(l.pop())
print(l.pop(2))
#remove function remove the value  list.remove(value)
print(l.remove(200))
# clear function  removes only the elements and not the list objects
# list.clear()[]
n=['p','k','y']
print(n.clear())
#del function delete all the element and the list object also
#del lst
#del lst[start:stop]
k=[11,23,15,24,12,26,29]
del k[0:3]
print(k)
del k
#print(k)
#count function list.count(value) -count the no of item found in the list
print(m.count(200))
#reverse function - l.reverse()
l.reverse()
print(l)
#len() function
print(len(l))
#max function
print(max(l))
#min function
print(min(l))
l.sort()
print(l)# asscending order
print(l.sort(reverse=True))# descending order



