def choose(n, k):
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return choose(n - 1, k - 1) + choose(n - 1, k)


if __name__ == '__main__':
    print(choose(6, 2))
