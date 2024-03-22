import math


class SquareGenerator:
    def __init__(self, start, end):
        if start > end:
            raise ValueError("Start value must be less than or equal to end value")
        self.start = start
        self.end = end

    def generate(self):
        return [i ** 2 for i in range(self.start, self.end + 1)]


def task2(start, end):
    print("~~~~~~~~~~~~~~~~~~~~~~ Task 2 ~~~~~~~~~~~~~~~~~~~~~~")
    result = [i ** 2 for i in range(start, end + 1)]
    print(result)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def main():
    print("~~~~~~~~~~~~~~~~~~~~~~ Task 1 ~~~~~~~~~~~~~~~~~~~~~~")
    squares_list = [i ** 2 for i in range(1, 11)]
    print(squares_list)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    task2(5, 20)

    print("~~~~~~~~~~~~~~~~~~~~~~ Task 3 ~~~~~~~~~~~~~~~~~~~~~~")
    square_generator = SquareGenerator(10, 50)
    generated_squares = square_generator.generate()
    print(generated_squares)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("~~~~~~~~~~~~~~~~ Task 4 and Task 5 ~~~~~~~~~~~~~~~~~")
    try:
        square_roots = [math.sqrt(number) for number in generated_squares]
        print(square_roots)
    except NameError:
        print("Square roots calculation skipped due to previous error.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


main()
