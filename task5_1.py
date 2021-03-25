my_file = open('file5_1.txt', 'a')

while True:
    user_input = input("Enter a string: ")
    if user_input == "":
        break
    my_file.writelines(user_input + '\n')

my_file.close()
