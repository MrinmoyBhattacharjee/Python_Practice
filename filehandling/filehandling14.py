#Python Program to Count the Number of vowels in a Text File
fname = input("Enter file name: ")
k = 0
f=open(fname,"r")
for line in f:
    words = line.split()
    for i in words:
        for letter in i:
         if (letter=='a'or letter=='i'or letter=='e'or letter=='o' or letter=='u'):
                    k = k + 1
print("Occurrences of Vowels:",k)
