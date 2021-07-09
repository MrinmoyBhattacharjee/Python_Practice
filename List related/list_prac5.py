l1=[11,3.45,4+5j,True,"Mrinmoy"]
#l2=[100,200,300]
#l3=l1+l2  # joining list
#print(l3)
#print(l2*3)#replicating a list

#slicing a list list_variable[start:stop:step] by default step 1
# it will work upto stop-1
l2=[11,22,33,44,55,66,77,88,99,100]
print("l2[1:4]",l2[1:4]) #list slicing
print("l2[3:-3]",l2[3:-3])
print("l2[3:]",l2[3:])
print("l2[:-2]",l2[:-2])
print("l2[:]",l2[:])
print("l2[::2]",l2[::2])
print("l2[:-3:3]",l2[:-3:3])
print("l2[::-1]",l2[::-1])
print(l2)
#list Modification
l1[2:5]=[17,18,19]
print("After modification l1",l1)


