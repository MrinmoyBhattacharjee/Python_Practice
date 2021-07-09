'''l=[]

n=int(input("Enter the no of values to be input="))
print("enter",str(n),"  values")
for i in range(n):
    x=int(input("Enter the value="))
    l.append(x)
print("Original List",l)'''
'''
l=eval(input("enter the list"))
L=len(l)
l1=[]
l2=[]
for i in range(L):
    for j in range(i+1,l+1):
        if (l[i]==l[j]):
          l1.append(l[i])
        else:
            l2.append(l[i])
    print(l2)
    print(l1)
    '''
l=eval(input("enter the list"))
m=[]
for i in l:
    if i not in m:
        m.append(i)
print(l)
print(m)