def bubble_sort(l):
    # We go through the list as many times as there are elements
    n = len(l)
    for i in range(n):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                # Swap
                l[j], l[j+1] = l[j+1], l[j]


l=eval(input("enter a list="))
print("before sorting=",l)
bubble_sort(l)  #function call

print("after sorting")
print(l)