import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def print_definition(self):
        print("A circle is a shape consisting of all points in a plane that are at a given distance, called the radius, from a given point, called the center.")


my_circle = Circle(3)

print("Perimeter of the circle:", my_circle.perimeter())
print("Area of the circle:", my_circle.area())
my_circle.print_definition()



