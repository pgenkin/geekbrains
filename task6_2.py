class Road:
    _length: float
    _width: float

    specific_mass: float = 25.0
    asphalt_thickness: float = 5.0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, length, width):
        return length * width * Road.specific_mass * Road.asphalt_thickness


street_length = float(input("Enter street length, meters: "))
street_width = float(input("Enter street width, meters: "))
street = Road(street_length, street_width)
print("Required asphalt mass, kg is: ", street.asphalt_mass(street_length, street_width) / 1000, "tons")

