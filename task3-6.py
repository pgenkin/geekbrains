def int_func(user_word):
    return user_word.capitalize()

input_text = input("Enter words in lower case separated by spaces: ")
input_text = input_text.split(' ')
output_text = ""
cap_word = ""
for every_word in input_text:
    cap_word = int_func(every_word)
    output_text = output_text + ' ' + cap_word
print(output_text)


