import time

class TrafficLights:
    __color: dict = {"red": 7, "yellow": 3, "green": 7}

    def __init__(self):
        self.running()

    def running(self):
        while True:
            for k in self.__color.keys():
                print(f"The traffic light is now {k}")
                time.sleep(self.__color.get(k))


street_lights = TrafficLights()
street_lights.running()

