l=[num if num<15 else num*2 for num in range(10,20)]
print(l)


R=["Ev" if num%2==0 else "od" for num in range(10,20)]
print(R)
r=[x**y for x in [10,5,2]for y in [2,3,4]]
print(r)