def fact(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    print("Factorial=",f)
#_main
n=int(input("Enter a number="))
fact(n)  #function call


