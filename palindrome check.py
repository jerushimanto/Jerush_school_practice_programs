word = input("Enter a word:")
word_rev=word[::-1]

if word.lower()==word_rev.lower():
       print("Yes. {} is a palindrome.".format(word))
else:
       print("No, {} is not a palindrome.".format(word))
