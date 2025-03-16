class mymath:
    def absolute(self, num):
        return abs(num)
    
    def average(self, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)