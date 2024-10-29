def push(s,i):
     s.append(i)
     display(s)
def pop(s):
     if s==[]:
          print("Underflow!!")
     else:
          s.pop(0)
          display(s)

def peek(s):
     if s==[]:
          print("The Queue is empty")
     else:
          print("Top element is {} and rear element is {}".format(s[0],s[-1]))
def display(s):
     if s==[]:
          print(None)
     elif len(s)==1:
            print(s[0],"<-Front,Rear")
     else:
          print(s[0],"<- Top")
          for i in range(1,len(s)-1):
               print(s[i])
          print(s[-1],"<- Rear")
Queue=[]
while True:
     print('''1.Push
2.Pop
3.Peek
4.Display
5.Exit''')
     opt=int(input("Enter your choice:"))
    
     if opt==1:
          item=input("Enter the item to add:")
          push(Queue,item)
     elif opt==2:
          pop(Queue)
     elif opt==3:
          peek(Queue)
     elif opt==4:
          display(Queue)
     elif opt==5:
          break
     else:
          print("Invalid choice\n"
                "Enter a choice from 1 to 5")

