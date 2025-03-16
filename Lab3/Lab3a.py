import sys

def factorial1(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial2(n - 1)

if len(sys.argv) != 3:
    print("Input: lab3a.py <iterative/recursive> <integer>")
    sys.exit(1)

method = sys.argv[1]
try:
    number = int(sys.argv[2])
except ValueError:
    print("Not an integer.")
    sys.exit(1)

if method == "iterative":
    print(factorial1(number))
elif method == "recursive":
    print(factorial2(number))
else:
    print("must be 'iterative' or 'recursive'.")