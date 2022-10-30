def to_squares(num_list, index):
    if index >= len(num_list):
        return num_list
    num_list[index] = to_squares(num_list, index + 1)[index] ** 2
    return num_list


if __name__ == '__main__':
    num_list = [1, 2, 3, 4, 5, 6]
    print(to_squares(num_list, 3))
