'''
Define a class, which have a class parameter and have a same instance parameter.

**Hints**: Define a instance parameter, need add it in init method 
You can init a object with construct parameter or set the value later
'''

class Animals:
    name = "Animal" # Class parameter name

    def __init__(self, name):
        self.name = name # instance parameter

Tigger = Animals("Tigger")
print("%s name is %s" % (Animals.name, Tigger.name))

