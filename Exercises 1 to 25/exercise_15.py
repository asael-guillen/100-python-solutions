'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''

user = input("Input: ")
user_1 = int(user)
user_2 = int(2*user)
user_3 = int(3*user)
user_4 = int(4*user)

print(user_1 + user_2 + user_3 + user_4)