l=eval(input("Enter the Numbers as a list:"))
print("The entered list is",l)
i=0
while i<len(l):
       if l[i]%2!=0:
              l.pop(i)
              i=0
       else:
              i+=1
                     
print("List after removing odd numbers is",l)
              
