"""
    CS5001-5003 Fall 2022
    Lab 07 -- Coding Practice 7-- Problem 1, formula
    (Bruce) Chuanzhao Huang / 
"""


def formula(x):
    if x <= 1:
        return 3
    else:
        return 2 * formula(x - 1) + 5


if __name__ == "__main__":
    print(formula(1))
