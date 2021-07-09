#Python Program to Read a Text File and Print all the Numbers Present in the Text File
def noofdigit():
 fname = input("Enter file name: ")

 f=open(fname,"r")
 for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if (letter.isdigit()):
                    print(letter)


noofdigit()