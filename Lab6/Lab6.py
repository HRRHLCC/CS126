import sys
from shapes import Point, Triangle, Diamond, Rectangle, Square

shapes = []

with open("Lab6-data.txt", 'r') as file:
    for line in file:
        parts = line.strip().split()
        shape_type = parts[0]
        symbol = parts[1]    
        if shape_type == 'P':
            shape = Point(symbol)
        elif shape_type == 'T':
            size = int(parts[2])
            shape = Triangle(symbol, size)
        elif shape_type == 'D':
            size = int(parts[2])
            shape = Diamond(symbol, size)
        elif shape_type == 'R':
            width = int(parts[2])
            height = int(parts[3])
            shape = Rectangle(symbol, width, height)
        elif shape_type == 'S':
            size = int(parts[2])
            shape = Square(symbol, size)
        shapes.append(shape)

for shape in shapes:
    shape.draw()
    print()