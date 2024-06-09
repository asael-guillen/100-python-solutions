'''
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

To override a method in super class, we can define a method with the same name in the super class.
'''

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

shape = Shape()
print(f"The area of the shape is {shape.area()}") 

square = Square(4)
print(f"The area of the square with length {square.length} is {square.area()}")
