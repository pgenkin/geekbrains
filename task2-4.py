phrase = input("Введите строку, разделяя слова пробелами: ")
# Создаем список, используя пробел в качестве разделителя элементов:
phrase_list = phrase.split(' ')
print(phrase)
print()

for index, word in enumerate(phrase_list):
# Если в слове больше 10 букв, сокращаем его до 10 первых букв.
    if len(word) > 10:
        word = word[:10]
    print(index, word)