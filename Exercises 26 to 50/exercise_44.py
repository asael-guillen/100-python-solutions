'''
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

Use if statement to judge condition.
'''

word = input("Your word: ")
word = word.lower()

if word == 'yes':
    print('Yes')
else:
    print('No')