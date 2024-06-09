'''
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
'''

power = dict()
def dict_power(n):
    for i in range(1, n+1):
        power[i] = i**2
    return power

n = dict_power(int(input("Ingrese el rango de valores para el diccionario: ")))
print(n)