def swap(a,b):
        global x,y
        x,y=b,a
        
x,y=int(input("Enter number 1: ")),int(input("Enter number 2: "))


swap(x,y)
print("after swaping x = {} and y={}".format(x,y))
