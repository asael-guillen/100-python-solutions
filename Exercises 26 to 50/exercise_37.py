'''
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
'''

def printList():
    l = list()
    for i in range(1, 21):
        l.append(i**2)
    for j in l:
        print(j)

printList()