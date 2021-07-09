'''def rev(s,l):
    if l>0:
        print(s[l],end="")
        rev(s,l-1)
    elif l==0:
        print(s[0])
'''
def rev(s,n):
    if n==0:
     return s[0]
    else:
        return s[n]+rev(s,n-1)

s=input("enter the string=")
l=len(s)-1
print(rev(s,l))