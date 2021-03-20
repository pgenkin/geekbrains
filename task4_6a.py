from itertools import count

first_number = int(input("Enter the starting number: "))
last_number = int(input("Enter the last number: "))
for el in count(first_number):
    if el > last_number:
        break
    else:
        print(el)
        