def my_func(a, b, c):
    numbers_sorted = sorted([a, b, c])
    return numbers_sorted[1] + numbers_sorted[2]


number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
number_3 = float(input("Enter the third number: "))
print("The sum of two largest numbers is ", my_func(number_1, number_2, number_3))
