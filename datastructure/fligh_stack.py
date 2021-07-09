

def push (stack,item):
    stack.append(item)
    top=len(stack)-1

def Pop(stack):
    if stack==[]:
        return "Underflow"
    else:
        item=stack.pop()
        if len(stack)==0:
            top=None
        else:
            top=len(stack)-1

        return item

def Display(stack):
        if stack == []:
            print("Stack is Empty")
        else:
            top = len(stack) - 1
            print(stack[top], "<-top")
            for i in range(top - 1, -1, -1):
                print(stack[i])
#main
stack=[]
top=None
while True:
     print("1-push")
     print("2-pop")
     print("3-display")
     print("4-exit")
     ch=int(input("enter your choice betwn(1 to4)"))
     if ch==1:
         fno=int(input("enter the flight no.="))
         fname=input("enter the fight name=")
         fprice=int(input("enter the price="))
         item=[fno,fname,fprice]
         push(stack,item)
     elif ch==2:
          item=Pop(stack)
          if item =="Underflow":
           print("underflow,stack is empty")
          else:
           print("item deleted=",item)
     elif ch==3:
          Display(stack)
     elif ch==4:
           break
     else:
          print("invalid choice")
