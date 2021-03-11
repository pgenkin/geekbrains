rating_list = [7, 5, 3, 3, 2]
user_entry = int(input("Введите натуральное число: "))
rating_list.append(user_entry)
rating_list.sort(reverse = True)
print(rating_list)
