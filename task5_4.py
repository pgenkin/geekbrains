my_file_eng = open('file5_4.txt', 'r')
my_file_ru = open('file5_4_1.txt', 'a')


for line in my_file_eng:
    numbers_string = line.split('-')
    number_eng, number_number = numbers_string[0], numbers_string[1]
    if int(number_number) == 1:
        number_eng = "Один"
    elif int(number_number) == 2:
        number_eng = "Два"
    elif int(number_number) == 3:
        number_eng = "Три"
    else:
        number_eng = "Четыре"
    my_file_ru.write(number_eng + "-" + number_number)

my_file_eng.close()
my_file_ru.close()