'''
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

Use def methodName(self) to define a method.
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

circle = Circle(5)
print(f"The area of the circle with radius {circle.radius} is {circle.area()}")