from math import factorial


def fact(n):
    for element in range(n):
        yield factorial(element+1)


n = int(input("Enter a number: "))

for el in fact(n):
    print(el)