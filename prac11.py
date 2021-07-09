a=int(input("enter a number = "))
count=0
i=1
for i in range(1,a+1):
    if(a%i==0):
     count=count+1
    i=i+1
if(count==2):
    print("prime number")
else:
    ("not prime")

