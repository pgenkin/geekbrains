def string_processing():

#Считываем строку, используя пробелы в качестве разделителей.  Каждое символ становится элементом списка.
#Вычисляется сумма чисел в строке.  Если вместо числа (ASCII-код от 48 до 57) введен какой-либо другой символ,
#функция прекращает свою работу.

    global string_number_sum
    string_number_sum = 0
    input_text = input("Enter numbers 0 through 9 separated by spaces: ")
    input_text = input_text.split(' ')
    numbers_list = []
    for every_number in input_text:
        numbers_list.append(every_number)
        ord_value = ord(every_number)
        if ord_value not in range(48, 57):
            print("Illegal Character")
            break
        string_number_sum = string_number_sum + int(every_number)
    return string_number_sum

total_number_sum = 0
print("Press Enter to begin or any other key to abort.")
user_input = input()

while user_input == "":
    string_processing()
    total_number_sum = total_number_sum + string_number_sum
    print("Total sum is", total_number_sum)
    print("Press Enter to enter another string of numbers.  Press any other character to abort.")
    user_input = input()
    if user_input > "":
        print("Program stopped. Total sum is", total_number_sum)
        break