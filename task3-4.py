def degrees_1(x, y):
    return x ** y

def degrees_2(x, y):
    c = 1
    i = 1
    while i <= abs(y):
        c = c * x
        i += 1
    return 1 / c

number_1 = float(input("Enter a positive real number: "))
number_2 = int(input("Enter a negative integer: "))
print(degrees_1(number_1, number_2))
print(degrees_2(number_1, number_2))
