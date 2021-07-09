#Python Program to Count the Number of Lines in a Text File
fname = input("Enter file name: ")
num_lines = 0
f=open(fname, 'r')
for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)