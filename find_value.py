def find_value(str_list, target_str):
    if len(str_list) == 0:
        return False
    if str_list[0] == target_str:
        return True
    return find_value(str_list[1:], target_str)


if __name__ == '__main__':
    str_list = ["a", "b", "c", "d", "e", "f", "g"]
    print(find_value(str_list, "e"))
