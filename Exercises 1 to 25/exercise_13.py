'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

user = input("Input: ")
d={"LETTERS":0, "DIGITS":0}

for char in user:
    if char.isalpha():
        d["LETTERS"] += 1
    elif char.isdigit():
        d["DIGITS"] += 1
    else:
        pass
    
print("LETTERS:",d["LETTERS"])
print("DIGITS:",d["DIGITS"])