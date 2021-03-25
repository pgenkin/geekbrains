my_file = open('file5_3.txt', 'r')

for line in my_file:
    employee_record = line.split()
    employee_name, employee_salary = employee_record[0], employee_record[1]
    if int(employee_salary) < 20000:
        print(employee_name, employee_salary)

my_file.close()