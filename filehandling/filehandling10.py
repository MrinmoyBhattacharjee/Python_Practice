#Python Program to Copy the Contents of One File into Another
f=open("Student.txt")
f1=open("Test.txt","w")
for line in f:
     f1.write(line)
f1.close()
f.close()

