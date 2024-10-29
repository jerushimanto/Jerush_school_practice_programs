f=open(r"F:\PYTHON\text with a.txt",'r')
l=[]
for i in f:
       if 'a' in i:
              l.append(i)
f.close()

f=open(r"F:\PYTHON\no a.txt",'w')
for i in l:
       f.write(i)
f.close()

       
