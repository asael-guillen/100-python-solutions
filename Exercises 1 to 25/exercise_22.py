'''
Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''

diccionario = {}

user = input("Input: ")
user_list = sorted(user.split(" "))

diccionario = dict(zip(user_list,map(lambda x: user_list.count(x),user_list)))
formatted_data = "\n".join(f"{key}:{value}" for key, value in diccionario.items())

print(formatted_data)