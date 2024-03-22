import math
from square_generator import SquareGenerator


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
