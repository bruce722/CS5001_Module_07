"""
    CS5001-5003 Fall 2022
    Lab 07 -- Coding Practice 7-- Problem 2, factorial
    (Bruce) Chuanzhao Huang / 
"""


def factorial(n):
    if n > 0:
        if n == 1:
            return 1
        else:
            product = factorial(n - 1) * n
        return product
    else:
        return 0


if __name__ == "__main__":
    print(factorial(2))
