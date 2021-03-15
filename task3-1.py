def division(a, b):
    try:
        print("The division result is ", a / b)
        return
    except ZeroDivisionError:
        print("Zero division is illegal")
        return


number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
division(number_1, number_2)