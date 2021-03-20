#Скрипт вызывается из терминала как python3 task4_1.py <employee_rate> <employee_hours> <employee_bonus>

from sys import argv


def salary_calc(rate, hours, bonus):
    try:
        return (rate*hours) + bonus
    except TypeError:
        return


script_name, employee_rate, employee_hours, employee_bonus = argv

print("The employee salary is, $ ", salary_calc(int(employee_rate), int(employee_hours), int(employee_bonus)))
