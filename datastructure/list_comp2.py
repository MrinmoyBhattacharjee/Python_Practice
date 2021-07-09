l=[i  for i in range(1,10) if i%2==0]

#print(l)

l=[(x,y) for x in range(15) if (x%3==0) for y in range(15) if (y%2==1)]
print(l)