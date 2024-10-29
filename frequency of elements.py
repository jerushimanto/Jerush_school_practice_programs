l1=eval(input("Enter the list:"))
l2=[]
for i in l1:                            
       if i not in l2:
              l2.append(i)

for i in l2:
       cou=l1.count(i)
       print("Number of {} in the list is {}".format(i,cou))
