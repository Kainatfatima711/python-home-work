class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius


# Creating an object of Circle
circle1 = Circle(5)  # You can change the radius here

print("Radius:", circle1.radius)
print("Area of Circle:", circle1.area())
print("Perimeter of Circle:", circle1.perimeter())