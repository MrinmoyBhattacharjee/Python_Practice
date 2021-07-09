#Python Program to Read a File and Capitalize the First Letter of Every Word in the File
fname = input("Enter file name: ")
f=open(fname,"r")

for line in f:
 l = line.title()
 print(l)