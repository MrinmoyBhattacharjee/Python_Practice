string=input("Enter string:")
#############first method#############
l=0
for ch in string:
         l=l+1
ns=string[0:2]+string[l-2:l]
print(ns)

################second method############
l=len(string)
ns=string[0:2]+string[l-2:l]
print(ns)