test_list = [300, 2, 12, 44, 1, 1, 4, 7, 1, 78, 123, 55]


def filter_func(user_list):
    n = len(user_list)
    filtered_list = []
    i = 1
    while i < n:
        if user_list[i] > user_list[i-1]:
            filtered_list.append(user_list[i])
        i += 1
    return filtered_list


new_list = filter_func(test_list)
print(new_list)
