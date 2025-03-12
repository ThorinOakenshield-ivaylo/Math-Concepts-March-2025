"""
    This file is for experimentation
"""


def fibonacci_recursive(n: int) -> int:
    if n == 0:
        return 0

    elif n == 1:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print([fibonacci_recursive(n) for n in range(int(input("Your number: ")))])

# import math
# from typing import Tuple, List
#
#
# def roots_solver(a: int, b: int, discriminant: int) -> Tuple[float, float]:
#     x1 = (-b + math.sqrt(discriminant)) / (2 * a)
#     x2 = (-b - math.sqrt(discriminant)) / (2 * a)
#
#
#     if x1 > x2:
#         return x1, x2
#
#     return x2, x1
#
#
# def solve_quadratic_equation(a: int, b: int, c: int) -> List[float]:
#     discriminant = b ** 2 - 4 * a * c
#
#     if discriminant > 0:
#         x1, x2 = roots_solver(a, b, discriminant)
#
#         return [x1, x2]
#
#     elif discriminant == 0:
#         x = -b / (2 * a)
#
#         return [x]
#
#     else:
#         return []
#
#
# # Testing: Execute this cell. The outputs should match the expected outputs. Feel free to write more tests
# print(solve_quadratic_equation(1, -1, -2)) # [-1.0, 2.0]
# print(solve_quadratic_equation(1, -8, 16)) # [4.0]
# print(solve_quadratic_equation(1, 1, 1)) # []