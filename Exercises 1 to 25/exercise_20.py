'''
Define a class with a generator which can iterate the numbers, 
which are divisible by 7, between a given range 0 and n.
'''

class Iterator:
    @staticmethod
    def generator(n):
        for i in range(1,n+1):
            if i % 7 == 0:
                yield i

gen = Iterator.generator(42)

for number in gen:
    print(number)