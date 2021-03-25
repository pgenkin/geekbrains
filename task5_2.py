my_file = open('file5_2.txt', 'r')

for line in my_file:
    print("There are", line.count(' ') + 1, "words in the line.")

my_file.seek(0)
total_lines = len(my_file.readlines())
print("There are", total_lines, "lines in the file.")

my_file.close()
