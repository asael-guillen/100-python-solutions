'''
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.
'''

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = list(filter(lambda x: x % 2 == 0, my_list))
print(evenNumbers)