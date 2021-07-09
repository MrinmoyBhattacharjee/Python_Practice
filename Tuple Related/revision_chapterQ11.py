#Write a program to sort a dictionary’s keys using Bubble sort and produce the sorted keys as a list.
def bubble_sort(n):
    for i in range(1,len(n)):
        for j in range(len(n)-i):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n
dic={'c':11,'e':22,'f':12,'a':20}
n=list(dic.keys())
print(bubble_sort(n))
