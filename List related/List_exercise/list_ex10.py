#(c) The list [‘a’,’bb’,’ccc’,’dddd’, . . . ] that ends with 26 copies of the letter z.

l3 = []
al = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(al)):
    d=''
    d=(al[i]*(i+1))
    l3.append(d)
print('List  :',l3)