my_file = open('file5_5.txt', 'w')
number_sum = 0

user_input = input("Enter numbers separated by spaces: ")
my_file.write(user_input)
content = user_input.split()

for i in range(len(content)):
    number_sum = number_sum + int(content[i])

print(number_sum)
my_file.close()

