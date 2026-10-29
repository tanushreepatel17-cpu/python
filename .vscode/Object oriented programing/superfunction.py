#super() = function used in a child class to call methods from parent class (superclass)
#           allows you to extend the functionality of the inherited methods




class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square:
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle:
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle(color = "red", is_filled = True, radius = 5)
square = Square(color = "blue", is_filled = False, width = 7)
triangle = Triangle(color = "pink", is_filled = True, width = 6, height = 7)

print(circle.color)
print(circle.is_filled)
print(circle.radius)
print("---------------------------")

print(square.color)
print(square.is_filled)
print(f"{square.width}cm")
print("---------------------------")

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")
print("---------------------------")








