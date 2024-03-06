'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1, Y-1
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''
def generate_2d_array(X, Y):
    # Using list comprehension to generate the 2D array
    array_2d = [[i*j for j in range(Y)] for i in range(X)]
    return array_2d

# Example input
X, Y = 3, 5

# Generating and printing the 2D array
result = generate_2d_array(X, Y)
print(result)
