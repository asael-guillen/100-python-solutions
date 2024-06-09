'''
Define a class named American and its subclass NewYorker.

Use class Subclass(ParentClass) to define a subclass.
'''

class American:
    def __init__(self):
        self.nationality = "American"
    
    def say_hello(self):
        return "Hello from an American!"

class NewYorker(American):
    def __init__(self):
        super().__init__()
        self.city = "New York"
    
    def say_hello(self):
        return "Hello from a New Yorker!"

american = American()
new_yorker = NewYorker()

print(american.say_hello())
print(new_yorker.say_hello())
print(new_yorker.nationality)
print(new_yorker.city)
