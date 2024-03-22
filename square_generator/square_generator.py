from abc import ABC, abstractmethod


class SquareGenerator(ABC):
    def __init__(self, start, end):
        if start > end:
            raise ValueError("Start value must be less than or equal to end value")
        self.start = start
        self.end = end

    @abstractmethod
    def generate(self):
        pass


class CubicGenerator(SquareGenerator):
    def generate(self):
        if self.start > self.end:
            raise ValueError("Start value must be less than or equal to end value")
        return [i ** 3 for i in range(self.start, self.end + 1)]
