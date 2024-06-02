from math import sqrt, atan2, cos, sin


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def subtract(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def scale(self, other):
        return Complex(self.real * other, self.imaginary * other)

    def multiply(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary

        return Complex(real, imaginary)

    def c_sqrt(self):
        m = sqrt(sqrt(self.real**2 + self.imaginary**2))
        angle = atan2(self.imaginary, self.real) / 2

        return Complex(m*cos(angle), m*sin(angle))
