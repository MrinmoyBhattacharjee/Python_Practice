def Push(stack,item):
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
    if stack==[]:
        print("Stack is Empty")
    else:
        top=len(stack)-1
        print(stack[top],"<-top")
        for i in range(top-1,-1,-1):
            print(stack[i])
#_main
stack=[]
top=None  # initial value of top assign to  None
while True:
    print("Stack Operation Using List")
    print("1. For Push")
    print("2. For Pop")
    print("3. For Display")
    print("4. For Exit")
    ch=int(input("Enter your choice between (1 to 4):"))
    if ch==1:
        item=int(input("Enter the item to be push="))
        Push(stack,item)
    elif ch == 2:
        item=Pop(stack)
        if item=="Underflow":
            print("Underflow! Stack is Empty")
        else:
            print("Poped Item is=",item)
    elif ch == 3:
        Display(stack)
    elif ch==4:
        break
    else:
        print("Invalid Choice")
