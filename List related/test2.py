l=eval(input("enter the list"))
m=[]
for i in l:
    if i not in m:
        m.append(i)
print(l)
print(m)