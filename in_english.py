num_str_arr = ["zero", "one", "two", "three", "four", 
                "five", "six", "seven", "eight", "nine"]


def in_english(num):
    num = int(num)
    if num < 10:
        return num_str_arr[num]
    return in_english(num / 10) + " " + num_str_arr[num % 10]


if __name__ == '__main__':
    print(in_english(153))
