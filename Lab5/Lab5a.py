import sys
from reversemath import ReverseFloat

if len(sys.argv) != 3:
    print("Input: python lab5a.py <num1> <num2>")
else:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    a = ReverseFloat(num1)
    b = ReverseFloat(num2)

    print(f"{num1} + {num2} = {a + b}")
    print(f"{num1} - {num2} = {a - b}")
    print(f"{num1} x {num2} = {a * b}")
    print(f"{num1} / {num2} = {a / b}")