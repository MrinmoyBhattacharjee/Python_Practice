#to create a list using list comprehension ,consist of the cubes
#of the numbers 1 through 10 only if the cube is evenly divisable by 4
#Note: the cubed  no should be evenly divisable by 4 ,not the original no
l=[y for y in range(1,11) if y % 4 != 0 if y**3 % 4 == 0]
print(l)