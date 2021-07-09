#creating tuples

# empty tuple

T=tuple()
print(T)

#single Element
t1=(4)
print(t1)
print(type(t1))
t2=5,
print(t2)
print(type(t2))
#or using this way
t3=(10,) # we have specify a comma to create tuple with single element
print(t3)

#nested tuples
T2=(10,20,(100,200))
print(T2)

#create tuples from sequence
T3=tuple('welcome')
print(T3)

#create tuples from list
L=['H','E','L','L']
T4=tuple(L)
print(T4)

#tuples from user given values using tuple method
T5=tuple(input("enter tuple elements="))
print(T5)

#tuples from user given values using eval method
T6=eval(input("enter tuple elements="))
print(T6)
# Accessing tuple elements individualy
vowel=('a','e','i','o','u')
print(vowel[0])
print(vowel[1])
print(vowel[4])
print("#########################")
# Accessing tuple elements

value=('m','r','i','n','m','o','y')
for v in value:
    print(v)
#joining tuples
a=(5,7,9)
b=(34,67,89)
c=a+b
print(c)
#Replicating tuples

m=(10,20,30)*3
print("replicating tuples=",m)

#slicing tuples

tpl=(10,20,30,40,50,60,70,80,90,100)
print(tpl)
print(tpl[0:4])
print(tpl[0:7:3])
print(tpl[3:9:3])
print(tpl[::4])

#unpacking tuples
tp1=(1,2,'a','b')
w,x,y,z=tp1

print(w)
print(z)

#Deleting tuples (we cannot delete individual element from a tuples but a complete tuple
tp2=(10,20,30,40,50)
print(tp2)
del tp2
#print(tp2)

#len() method
tp2=(10,20,30,40,50)
print(len(tp2))

#max method applied on sequences of same type

tp2=(10,20,30,40,50)
print(max(tp2))

#min method applied on sequences of same type

tp2=(10,20,30,40,50)
print(min(tp2))

#count method applied on sequences of same type

tp2=(10,20,30,40,50,20,60)
print(tp2.count(20))

#index method

tp2=(10,20,30,40,50)
print(tp2.index(30))







