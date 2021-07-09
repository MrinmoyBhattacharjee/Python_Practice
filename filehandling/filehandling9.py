# Search Python Program to Count the Occurrences of a Word in a Text File
fname = input("Enter file name: ")
sr = input("Enter word to be searched:")
k = 0
f=open(fname, 'r')
for line in f:
    word=line.split()
    print(word)
    for i in word:
     if (i == sr):
           k = k + 1
print("Occurrences of the word:")
print(k)