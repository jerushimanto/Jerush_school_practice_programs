f=open(r"F:\PYTHON\XII CS Practicals\students.dat",'w')
a=0
while a!='':
       rnos=input('Enter the roll number of the student:')
       name=input("Enter the name of the student")
       marks=float(input('Enter the mark:'))
       val="{}:{}:{}".format(rnos,name,marks)
       f.write(val)
       a=input("Press any number to continue or press enter to finish")
f.close()

