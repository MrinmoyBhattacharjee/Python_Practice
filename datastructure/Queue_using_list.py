def Enqueue(queue,item):
    queue.append(item)
    if len(queue)==1:
        front=rear=0
    else:
        rear=len(queue)-1
def Dequeue(queue):
    if queue==[]:
        return "Underflow"
    else:
        item=queue.pop(0)
        if len(queue)==0:
            front=rear=None
        return item
def Display(queue):
    if queue==[]:
        print("Queue is Empty")
    elif len(queue)==1:

        print(queue[0],"<-Front,Rear")
    else:
        front=0
        rear=len(queue)-1
        print(queue[front],"<-Front")
        for i in range(1,rear):
            print(queue[i])
        print(queue[rear],"<--Rear")



#_main

queue=[]
front=rear=None  # initial value of assign to  None
while True:
    print("Queue Operation Using List")
    print("1. For Enqueue")
    print("2. For Dequeue")
    print("3. For Display")
    print("4. For Exit")
    ch=int(input("Enter your choice between (1 to 4):"))
    if ch==1:
        item=int(input("Enter the item ="))
        Enqueue(queue,item)
    elif ch == 2:
        item=Dequeue(queue)
        if item=="Underflow":
            print("Underflow! Queue is Empty")
        else:
            print("Dequeueed Item is=",item)
    elif ch == 3:
        Display(queue)
    elif ch==4:
        break
    else:
        print("Invalid Choice")
