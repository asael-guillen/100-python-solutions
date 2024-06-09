'''
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
'''

def even_odd(n):
    if n % 2 == 0:
        print(f"{n} is an even number")
    elif n % 2 != 0:
        print(f"{n} is an odd number")

even_odd(45)