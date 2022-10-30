"""
    CS5001-5003 Fall 2022
    Lab 07 -- Coding Practice 7-- Problem 4, lower_triangle
    (Bruce) Chuanzhao Huang / 
"""


def lower_triangle(n):
    if n > 0:
        if n == 1:
            print("*")
        else:
            lower_triangle(n - 1)
            print("*" * n)


if __name__ == "__main__":
    print(lower_triangle(4))
