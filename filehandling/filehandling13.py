#Python Program to Count the Number of Blank Spaces
# in a Text File
fname = input("Enter file name: ")
k = 0
f=open(fname,"r")
for line in f:
        words = line.split()
        print(words)
        for i in words:
            print(i)
            for letter in i:
                if (letter.isspace()):
                    k = k + 1
print("Occurrences of blank spaces:")
print(k)