def arithm(x,y):
       return x+y,x-y,x*y,x/y
x=float(input("Enter the number 1: "))
y=float(input("Enter the number 2: "))
print('sum =',arithm(x,y)[0],'\n'
      'diff =',arithm(x,y)[1])
