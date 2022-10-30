def find_max(num_list):
    return find_max_helper(num_list, 0)


def find_max_helper(num_list, index):
    if index >= len(num_list):
        return 0
    return max(find_max_helper(num_list, index + 1), num_list[index])


if __name__ == '__main__':
    num_list = [3, 5, 7, 6, 2, 1, 4]
    print(find_max(num_list))
