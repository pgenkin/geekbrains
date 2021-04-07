class MyMethod:
    e: int

    @staticmethod
    def data_check(element: str, user_list: list):
        try:
            e = int(element)
            print(e)
            user_list.append(e)
        except ValueError:
            print("It's a string.")


elements = []

while True:
    a = input("Enter the element: ")
    if a == "stop":
        break
    MyMethod.data_check(a, elements)

print("Here is the list of entered integer elements: ", elements)





