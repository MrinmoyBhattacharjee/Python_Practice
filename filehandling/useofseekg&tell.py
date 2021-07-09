#using readline
fobj2=open("Student.txt")
str=fobj2.readline() # returns a line in form of string
print(fobj2.tell())
print(str)
fobj2.seek(0)
str2=fobj2.readline()
print(str2)




