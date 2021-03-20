#Итератор повторяет элементы заданного программно списка, которые делятся на 3 без остатка.
from itertools import cycle

test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cycle_number = 0

for el in cycle([el for el in test_list if el % 3 == 0]):
    if cycle_number > 10:
        break
    print(el)
    cycle_number += 1


