# No of words in a given file
myfile=open("Student.txt")
c=0
for line in myfile:
    word=line.split()
    #print(word)
    for w in word:
        c = c + 1
print("No of Words=", c)
