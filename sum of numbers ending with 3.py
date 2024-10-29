l1=eval(input("Enter the numbers as a list:"))
l2=0
for i in l1:
       s=str(i)
       if s[-1]=='3':
              l2+=i
print("Sum of numbers ending with 3 are",l2)
       
