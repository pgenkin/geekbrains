user_entry = input("Please enter a positive integer: ")
number = int(user_entry)
modulus = 0
max_number = 0
i = 1

while i <= len(user_entry):
    modulus = number % 10
    if modulus > max_number:
        max_number = modulus
    number = number // 10
    i += 1

print(max_number)
