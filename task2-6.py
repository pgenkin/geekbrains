product_list = [] #Список, содержащий информацию о всех продуктах (номер позиции и кортеж со словарем)
product = [] #Временный список, из которого создается кортеж для каждого продукта.  После создания кортежа очищается.
product_name = [] #Список, содержащий названия по каждой позиции
product_price = [] #Cписок, содержащий цены по каждой позиции
product_quantity = [] #Cписок, содержащий количества по каждой позиции
product_units = [] #Cписок единиц измерения по каждой позиции
n = int(input("Введите количество товаров: "))
i = 0

#Вводим данные по каждой позиции и создаем словарь для каждой из них:
while i < n:
    product_name.append(input("Название: "))
    product_price.append(int(input("Цена: ")))
    product_quantity.append(int(input("Количество: ")))
    product_units.append(input("Единица измерения: "))
    product_dictionary = {"Название": product_name[i], "Цена": product_price[i], "Количество": product_quantity[i],
                          "Ед.": product_units[i]}
# Создаем кортеж для продукта, а затем элемент списка, состоящий из номера товарной позиции и ее кортежа:
    product.insert(0, i + 1)
    product.append(product_dictionary.items())
    product_list.append(tuple(product))
    product.clear()
    i += 1

print()
print("Список товаров:")
print(product_list)
analysis_dictionary = {"Название": product_name, "Цена": product_price, "Количество": product_quantity,
                       "Ед.": product_units[0]}
print()
print("Словарь для анализа данных:")
print(analysis_dictionary)

