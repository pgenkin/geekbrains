class ComplexNumber:
    def __init__(self, r_part: int, i_part: int):
        self.r_part = r_part
        self.i_part = i_part

    def __str__(self):
        if self.i_part > 0:
            return str(self.r_part) + " + " + str(self.i_part) + "i"
        else:
            return str(self.r_part) + " - " + str(abs(self.i_part)) + "i"

    def __add__(self, other):
        return ComplexNumber(self.r_part + other.r_part, self.i_part + other.i_part)

    def __mul__(self, other):
        return ComplexNumber(self.r_part * other.r_part - self.i_part * other.i_part, self.r_part * other.i_part + self.i_part * other.r_part)


print("First complex number:")
real_part1 = int(input("Enter the real part: "))
imaginary_part1 = int(input("Enter the imaginary part: "))
number1 = ComplexNumber(real_part1, imaginary_part1)

print("Second complex number:")
real_part2 = int(input("Enter the real part: "))
imaginary_part2 = int(input("Enter the imaginary part: "))
number2 = ComplexNumber(real_part2, imaginary_part2)

print("The sum of complex numbers is ", ComplexNumber.__add__(number1, number2))
print("The product of complex numbers is ", ComplexNumber.__mul__(number1, number2))