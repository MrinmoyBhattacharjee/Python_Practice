#wap to count no of vowels of a given string
string=input("enter the string=")
c=0

vowel=('aeiou')
for letter in string:
    if letter in vowel:
        c=c+1
print(c)

