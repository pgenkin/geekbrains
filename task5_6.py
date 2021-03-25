my_file = open('file5_6.txt')
my_dict = {}

for line in my_file:
    course = line.split()

    for i in range(len(course)):
        if course[i] == '-':
            course[i] = "0"

    course_name = course[0].replace(':', '')
    lectures = course[1].replace('(l)', '')
    practical = course[2].replace('(pr)', '')
    labs = course[3].replace('(lab)', '')
    total_hours = int(lectures) + int(practical) + int(labs)
    my_dict.update({course_name: total_hours})

print(my_dict)
my_file.close()