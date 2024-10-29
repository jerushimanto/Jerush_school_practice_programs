sentence=input("Enter the sentence you want to check:")
alpha=ualpha=lalpha=num=space=symbol=0
others={}

for letter in sentence:
       if letter.isalpha():
              alpha+=1
              if letter.isupper():
                     ualpha+=1
              elif letter.islower():
                     lalpha+=1
       elif letter.isdigit():
              num+=1
       elif letter.isspace():
              space+=1
       else:
              symbol+=1

print('''Number of alphabets in the sentence are:{}

Number of uppercase alphabets in the sentence are:{}

Number of lowercase alphabets in the sentence are:{}

Number of numerals in the sentence are:{}

Number of space in the sentence are:{}

Number of special characters are:{}'''.format(alpha,ualpha,lalpha,num,space,symbol))


              
              
                    
