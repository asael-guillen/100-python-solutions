# 100-python-solutions
Solution to 100 python exercises from: https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises%20for%20Python%203.md


## ------------------ Level 1 ------------------

### Exercise 1

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

### Exercise 2

Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

### Exercise 3

With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included) and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

**Hints**:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()

### Exercise 4

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

**Hints**:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple.

### Exercise 5

Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

**Hints**:
Use __init__ method to construct some parameters

## ------------------ Level 2 ------------------

### Exercise 6

Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

**Hints**:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input.

### Exercise 7

Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

**Hints**:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

### Exercise 8

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

### Exercise 9

Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

### Exercise 10

Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

**Hints**:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.

### Exercise 11

Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

### Exercise 12

Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

### Exercise 13

Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

### Exercise 14

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

### Exercise 15

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

### Exercise 16

Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

### Exercise 17

Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

## ------------------ Level 3 ------------------

### Exercise 18

A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12

Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example:
If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345

Then, the output of the program should be:
ABd1234@1

### Exercise 19

You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

**Hints**:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use itemgetter to enable multiple sort keys.

### Exercise 20

Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

**Hints**:
Consider use yield

### Exercise 21

A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 ¡­ The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2

### Exercise 22

Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
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

## ------------------ Level 1 ------------------

### Exercise 23

Write a method which can calculate square value of number

**Hints**: Using the ** operator

### Exercise 24

Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function 
**Hints**: The built-in document method is doc

### Exercise 25

Define a class, which have a class parameter and have a same instance parameter.

**Hints**: Define a instance parameter, need add it in init method You can init a object with construct parameter or set the value later

### Exercise 26

Define a function which can compute the sum of two numbers.

**Hints**: Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

### Exercise 27

Define a function that can convert a integer into a string and print it in console.

**Hints**: Use str() to convert a number to string.

### Exercise 28

Define a function that can convert a integer into a string and print it in console.

**Hints**: Use str() to convert a number to string.

### Exercise 29

Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

### Exercise 30

Define a function that can accept two strings as input and concatenate them and then print it in console.

### Exercise 31

Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

### Exercise 32

Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

### Exercise 33

Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

**Hints**:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.

### Exercise 34

Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

**Hints**:

Use dict[key]=value pattern to put entry into a dictionary. Use ** operator to get power of a number. Use range() for loops.

### Exercise 35

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

**Hints**:

Use dict[key]=value pattern to put entry into a dictionary. Use ** operator to get power of a number. Use range() for loops. Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

### Exercise 36

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

**Hints**:

Use dict[key]=value pattern to put entry into a dictionary. Use ** operator to get power of a number. Use range() for loops. Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

### Exercise 37

Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number. Use range() for loops. Use list.append() to add values into a list.

### Exercise 38

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

**Hints**:

Use ** operator to get power of a number. Use range() for loops. Use list.append() to add values into a list. Use [n1:n2] to slice a list

### Exercise 39

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

**Hints**:

Use ** operator to get power of a number. Use range() for loops. Use list.append() to add values into a list. Use [n1:n2] to slice a list

### Exercise 40

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

**Hints**:

Use ** operator to get power of a number. Use range() for loops. Use list.append() to add values into a list. Use [n1:n2] to slice a list

### Exercise 41

Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

**Hints**:

Use ** operator to get power of a number. Use range() for loops. Use list.append() to add values into a list. Use tuple() to get a tuple from a list.

### Exercise 42

With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 

**Hints**:

Use [n1:n2] notation to get a slice from a tuple.

### Exercise 43

Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 

**Hints**:

Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.

### Exercise 44

Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

**Hints**:

Use if statement to judge condition.

### Exercise 45

Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

**Hints**:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.

### Exercise 46



### Exercise 47



### Exercise 48



### Exercise 49



### Exercise 50



### Exercise 51



### Exercise 52



### Exercise 53



### Exercise 54



### Exercise 55



### Exercise 56



### Exercise 57



### Exercise 58



### Exercise 59



### Exercise 60



### Exercise 61



### Exercise 62



### Exercise 63



### Exercise 64



### Exercise 65



### Exercise 66



### Exercise 67



### Exercise 68



### Exercise 69



### Exercise 70



### Exercise 71



### Exercise 72



### Exercise 73



### Exercise 74



### Exercise 75



### Exercise 76



### Exercise 77



### Exercise 78



### Exercise 79



### Exercise 80



### Exercise 81



### Exercise 82



### Exercise 83



### Exercise 84



### Exercise 85



### Exercise 86



### Exercise 87



### Exercise 88



### Exercise 89



### Exercise 90



### Exercise 91



### Exercise 92



### Exercise 93



### Exercise 94



### Exercise 95



### Exercise 96



### Exercise 97



### Exercise 98



### Exercise 99



### Exercise 100