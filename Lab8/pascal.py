class Pascal:
    def __init__(self):
        self.data = {}
    def get_value(self, row, col):
        if col < 0 or col > row:
            return 0
        if (row, col) in self.data:
            return self.data[(row, col)]
        if col == 0 or col == row:
            self.data[(row, col)] = 1
            return 1
        value = self.get_value(row - 1, col - 1) + self.get_value(row - 1, col)
        self.data[(row, col)] = value
        return value
    def display_triangle(self, lines):
        for row in range(lines):
            print(' ' * (lines - row), end='')
            for col in range(row + 1):
                print(f'{self.get_value(row, col):4}', end=' ')
            print()

pascal = Pascal()
num_lines = int(input("Enter number of lines: "))
pascal.display_triangle(num_lines)