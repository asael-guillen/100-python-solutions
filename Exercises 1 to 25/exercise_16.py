'''
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''

user = input("Input: ")
num_list = user.split(",")

odd_list = []

for i in num_list:
    if int(i)%2 != 0:
        odd_list.append(i)
    else:
        pass

print(','.join(odd_list))