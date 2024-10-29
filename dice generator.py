import random as r
import time 
a=''
while a=='':
       num=r.randint(1,6)
       time.sleep(2)
       print(num)
       print()
       time.sleep(0.5)
       a=input("press Enter to roll the dice or q and enter to exit")
       
