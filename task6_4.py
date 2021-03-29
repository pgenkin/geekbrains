class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self):
        print("The car has started.")

    def car_stop(self):
        print("The car has stopped.")

    def car_right(self):
        print("The car has turned right.")

    def car_left(self):
        print("The car has turned left.")

    def car_show_speed(self):
        print(f"The car speed is {self.speed}")


class TownCar(Car):

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def car_show_speed(self):
        print("This is town car.")
        print(f"The car speed is {self.speed}")
        if self.speed > 60:
            print("The car speed is above speed limit.")


class WorkCar(Car):

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def car_show_speed(self):
        print("This is a work car.")
        print(f"The car speed is {self.speed}")
        if self.speed > 40:
            print("The car speed is above speed limit.")


class SportCar(Car):

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


test_car_1 = TownCar(70, "grey", "Ford", False)
test_car_1.car_show_speed()
print("The color is", test_car_1.color)
print("The name is", test_car_1.name)
print()
test_car_2 = WorkCar(42, "green", "Mercedes", False)
test_car_2.car_show_speed()
print("The color is", test_car_2.color)
print("The name is", test_car_2.name)
print()
test_car_3 = SportCar(90, "red", "Lamborghini", False)
print("This is a sport car.")
test_car_3.car_show_speed()
print("The color is", test_car_3.color)
print("The name is", test_car_3.name)
print()
test_car_4 = PoliceCar(55, "blue", "Dodge", True)
print("This is a police car.")
test_car_4.car_show_speed()
print("The color is", test_car_4.color)
print("The name is", test_car_4.name)

