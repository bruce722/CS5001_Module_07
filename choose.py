def choose(k, n):
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return choose(k - 1, n - 1) + choose(k, n - 1)


if __name__ == '__main__':
    print(choose(2, 6))
