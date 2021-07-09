s=input("Enter string:")
uc=0
lc=0
a=0
n=0
for ch in s:

    if(ch.isupper()):
        uc=uc+1
    elif(ch.islower()):
        lc=lc+1
    elif(ch.isdigit()):
        n=n+1
    if(ch.isalpha()):
        a=a+1
print("No of alphabet=",a)
print("No of lowercase=",lc)
print("No of uppercase=",uc)
print("No of numeric=",n)


