"""
    CS5001-5003 Fall 2022
    Lab 07 -- Coding Practice 7-- Problem 3, upper_triangle
    (Bruce) Chuanzhao Huang / 
"""


def upper_triangle(n):
    if n > 0:
        if n == 1:
            print("*")
        else:
            print("*" * n)
            upper_triangle(n - 1)
