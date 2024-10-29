def push(s,i):
     s.append(i)
     display(s)
def pop(s):
     if s==[]:
          print("Underflow!!")
     else:
          s.pop(-1)
          display(s)
def peek(s):
     if s==[]:
          print("The stack is empty")
     else:
          print("Top element is",s[-1])
def display(s):
     if s==[]:
          print(None)
     else:
          print(s[-1],"<- Top")
          for i in range(len(s)-2,-1,-1):
               print(s[i])
          
#main
Stack=[]

while True:
     print('''1.Push
2.Pop
3.Peek
4.Display
5.Exit''')
     opt=int(input("Enter your choice:"))
     if opt==1:
          item=input("Enter the item to add:")
          push(Stack,item)
     elif opt==2:
          pop(Stack)
     elif opt==3:
          peek(Stack)
     elif opt==4:
          display(Stack)
     elif opt==5:
          break
     else:
          print("Invalid choice\n"
                "Enter a choice from 1 to 5")
     print()
          
             

     
