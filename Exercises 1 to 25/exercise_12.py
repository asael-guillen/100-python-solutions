'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

# Defining a function to check if all digits in a number are even
def all_digits_even(n):
    return all(int(digit) % 2 == 0 for digit in str(n))

# Generating and filtering the list of numbers between 1000 and 3000 where all digits are even
even_digit_numbers = [str(number) for number in range(1000, 3001) if all_digits_even(number)]

# Joining the numbers into a comma-separated string
result = ', '.join(even_digit_numbers)
print(result)