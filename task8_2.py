class DivisionByZero(Exception):
    def __init__(self, text: str):
        self.text = text


try:
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    if b == 0:
        raise DivisionByZero("Illegal Operation: A Zero Division Error.")

    c = a / b
    print("a / b = ", c)

except DivisionByZero as err:
    if ZeroDivisionError:
        print(err)

