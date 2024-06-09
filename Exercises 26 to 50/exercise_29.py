'''
Define a function that can receive two integral numbers in string form and 
compute their sum and then print it in console.
'''

def suma_int(n, m):
    return int(n) + int(m)

user_1 = input("Ingrese el primer numero: ")
user_2 = input("Ingrese el segundo numero: ")

print("La suma es:", suma_int(user_1, user_2))