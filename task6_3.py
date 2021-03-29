class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name: str, surname: str, position: str, income: dict):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(f"The full name is {self.name} {self.surname}")

    def get_total_income(self):
        a = list(self._income.values())
        print(f"Total income for {self.name} {self.surname}, {self.position} is", a[0] + a[1])


test_user_1 = Position("John", "Doe", "welder", {"wage": 500, "bonus": 100})
test_user_2 = Position("Jane", "Doe", "clerk", {"wage": 300, "bonus": 50})
test_user_1.get_full_name()
test_user_1.get_total_income()
print()
test_user_2.get_full_name()
test_user_2.get_total_income()



