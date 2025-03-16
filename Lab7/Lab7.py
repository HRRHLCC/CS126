import sys
from shapes import Triangle, Diamond, Rectangle, Square

shapes = []

def parse_line(line):
    parts = line.strip().split()
    shape_type = parts[0]
    symbol = parts[1]

    if shape_type == "T":
        size = int(parts[2])
        return Triangle(symbol, size)
    elif shape_type == "D":
        size = int(parts[2])
        return Diamond(symbol, size)
    elif shape_type == "R":
        width = int(parts[2])
        height = int(parts[3])
        return Rectangle(symbol, width, height)
    elif shape_type == "S":
        size = int(parts[2])
        return Square(symbol, size)


with open("Lab7-data.txt", 'r') as file:
    for line in file:
        shape = parse_line(line)
        if shape:
            shapes.append(shape)

for shape in shapes:
    shape.draw()
    print()  # Add space between shapes