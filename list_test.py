int_list = [1, 2, 3, 4, 5]

# Convert list to string
list_str = ','.join(map(str, int_list))

# Convert string back to list of integers
converted_list = list(map(int, list_str.split(',')))

print(converted_list)