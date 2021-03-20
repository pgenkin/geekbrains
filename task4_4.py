from collections import Counter

initial_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

item_count = Counter(initial_list)
unique_list = [el for el in initial_list if item_count[el] == 1]
print(unique_list)