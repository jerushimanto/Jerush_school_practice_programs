f=open(r"F:\PYTHON\poem.txt",'r')
c=0
a=0
for i in f:
       c+=1
       a+=len(i)
print("Number of lines in the file is",c)
print("Size of the file is",a,"bytes")
f.close()


