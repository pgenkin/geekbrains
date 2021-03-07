a = int(input("First day distance: "))
b = int(input("Desired daily distance: "))
result = a
#print("{:.2f}".format(result))
days = 1

while result < b:
    result = result + result * 0.1
    days = days + 1
#    print("{:.2f}".format(result))

print("Desired daily distance will be run in", days, "days.")