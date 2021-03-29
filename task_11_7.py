class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        ans_r = self.r + other.r
        ans_i = self.i + other.i
        return f'{ans_r} + {ans_i}j'

    def __mul__(self, other):
        ans_r = self.r * other.r - self.i * other.i
        ans_i = self.r * other.i + other.r * self.i
        return f'{ans_r} + {ans_i}j'


val1 = Complex(3, 90)
val2 = Complex(5, 2)
print(val1 + val2)
print(val1 * val2)
