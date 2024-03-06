'''
Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. 
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''

def factorial(n):
    resultado = 1
    if n > 1:
        resultado *= n*factorial(n-1)
    else:
        return resultado
    
    return resultado

n = int(input("Ingrese el valor: "))
print(f"El factorial de {n} es: " + str(factorial(n)))