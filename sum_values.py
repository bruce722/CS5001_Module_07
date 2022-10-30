def sum_values(num_list, index):
  if index >= len(num_list):
    return 0
  return sum_values(num_list, index + 1) + num_list[index]


if __name__ == '__main__':
  num_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  print(sum_values(num_list, 9))
