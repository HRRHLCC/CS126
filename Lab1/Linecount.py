import sys

def count_lines(filename):
    with open(filename, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines in {filename}: {len(lines)}")

if len(sys.argv) != 2:
    print("input: Lab1.py <filename>")
else:
     count_lines(sys.argv[1])