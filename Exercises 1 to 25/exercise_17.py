'''
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
'''
condition = True
d = {"deposit": 0}
while condition:
    user = input("D for deposit / W for withdrawal: ")
    if user == "D":
        amount = int(input("    Amount: "))
        d["deposit"] += amount
    elif user == "W":
        amount = int(input("    Amount: "))
        d["deposit"] -= amount
    else:
        condition = False
print("Balance:", d["deposit"])