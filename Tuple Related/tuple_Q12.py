import math
sumOfNum=0
mean=0
numTuple=(1,2,3,4,5)
print("The tuple is: ")
print(numTuple)
#sumOfNum=sum(numTuple)
mean=sum(numTuple)/len(numTuple)

print("Its mean is: ")
print(mean)

diff1=0
#newlist=list(numTuple)
for i in numTuple:
 diff1=diff1+((i-mean)**2)
#diff1=math.sqrt(diff1)
diff1=math.sqrt(diff1/(len(numTuple)-1))

print('Standard deviation:', "{0:.2f}".format(diff1))
