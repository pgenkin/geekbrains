# Используем словарь:
month_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето",
          7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}

month = int(input("Введите номер от 1 до 12: "))
print(month_dict.setdefault(month))

# Используем список:
month_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето",
              "Осень", "Осень", "Осень", "Зима"]
print(month_list[month-1])