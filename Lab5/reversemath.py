class ReverseFloat:
    def __init__(self, value):
        self.value = float(value)

    def __str__(self):
        return "%.2f" % self.value

    def __add__(self, other):
        # addition will perform subtraction
        return ReverseFloat(self.value - other.value)

    def __sub__(self, other):
        # subtraction will perform addition
        return ReverseFloat(self.value + other.value)

    def __mul__(self, other):
        # multiplication will perform division
        return ReverseFloat(self.value / other.value)

    def __truediv__(self, other):
        # division will perform multiplication
        return ReverseFloat(self.value * other.value)