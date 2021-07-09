tup1=((1,2),(3,4.15,5.15),(7,8,12,15))

(x,y,z)=tup1

mean1=float(sum(x))/len(x)
mean2=float(sum(y))/len(y)
mean3=float(sum(z))/len(z)

print("Mean of ", x ,"is : ",mean1 )
print("Mean of ", y ,"is : ", mean2)
print("Mean of ", z ,"is : ",mean3)
sumOfMeans=(mean1+mean2+mean3)/3
print("Sum of means: ", sumOfMeans)