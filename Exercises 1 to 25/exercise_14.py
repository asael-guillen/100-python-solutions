'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

d = {"up": 0, "low":0}
user = input("Input: ")

for char in user:
    if char.islower():
        d["low"] += 1
    if char.isupper():
        d["up"] += 1

print("UPPER CASE:", d["up"])
print("LOWER CASE:", d["low"])