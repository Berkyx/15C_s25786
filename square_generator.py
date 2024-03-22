class SquareGenerator:
    def __init__(self, start, end):
        if start > end:
            raise ValueError("Start value must be less than or equal to end value")
        self.start = start
        self.end = end

    def generate(self):
        return [i ** 2 for i in range(self.start, self.end + 1)]

