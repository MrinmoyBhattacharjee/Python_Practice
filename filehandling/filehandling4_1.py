# if there is a multiple line in a file we can access lines using function readline()
# inside of a loop
myfile=open("Student.txt")
s=" "
while s:
    s=myfile.readline()
    print(s)
myfile.close()

# But using this method ,readline also read leading and trailing spaces and also newline
#character \n
# so we can access the lines in different way



