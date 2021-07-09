
import math

def func(low,up,len):
    list=[]
    step=((up-low) /(len-1))
    for i in range(len):
        list.append(low)
        low=low+step
    return list


low=int(input("Enter the starting point="))
up=int(input("Enter the ending point="))


len=4

v = func(low,up,len)
print(" ", v)