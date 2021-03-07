revenue = int(input("Enter company revenue, $: "))
expense = int(input("Enter company expense, $: "))
profit = revenue - expense

if profit > 0:
    print("Company is profitable.")
    print("Profit to earnings ratio is", "%.2f" % (profit / revenue))
    employee_count = int(input("Number of employees is "))
    print("Profit per employee is $", "%.2f" % (profit / employee_count))
else:
    print("Company is not profitable.")