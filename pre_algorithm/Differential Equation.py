class Constant:
    order = 1

    def __init__(self):
        self.order = Constant.order
        Constant.order += 1

    def __repr__(self):
        return f"c{self.order}"


class Polynomial:
    def __init__(self, *coeffs):  # coeff[n - 1] * x^(n - 1)+ ... + coeff[0]
        self.coeffs = coeffs
        self.degree = len(coeffs)

    def differentiate(self):
        return Polynomial(*[i * v for i, v in enumerate(self.coeffs) if i > 0])

    def integrate(self):
        return Polynomial(Constant(), self.coeffs[0], *[v / (i + 1) for i, v in enumerate(self.coeffs) if i > 0])

    def __str__(self):
        if not self.coeffs:
            return 0

        ans = []
        for i in range(len(self.coeffs) - 1, -1, -1):
            coeff = self.coeffs[i]
            if not coeff:
                continue

            if i == 1:
                ans.append(f"{coeff}x" if type(coeff) is Constant or coeff != 1 else "x")
            elif i == 0:
                ans.append(str(coeff))
            else:
                ans.append(f"{coeff}x^{i}" if type(coeff) is Constant or coeff != 1 else f"x^{i}")

        return ' + '.join(ans)

    def __call__(self, x):
        value = 0
        for i in range(len(self.coeffs)):
            value += self.coeffs[i] * x ** i

        return value

    # +, * 연산 구현
    def __add__(self, other):
        A, B = self.coeffs, other.coeffs
        if len(A) < len(B):
            A, B = B, A

        return Polynomial(*[A[i] + B[i] if i < len(B) else A[i] for i in range(len(A))])

    def mul(self, k):
        return Polynomial(*[k * c for c in self.coeffs])

    def __sub__(self, other):
        return self + other.mul(-1)

    def __mul__(self, other):
        result = [0] * (self.degree + other.degree - 1)
        for i in range(self.degree):
            for j in range(other.degree):
                result[i + j] += self.coeffs[i] * other.coeffs[j]

        return Polynomial(*result)


class Exponential:
    e = 2.718281828

    def __init__(self, A, a, b):  # Ae^{(a + bi)x}
        self.A = A
        self.a = a
        self.b = b


class Function:
    pass


def func_analyze(string):
    pass


if __name__ == "__main__":
    f1 = Polynomial(1, 2, 3, 4)
    print(f1)
    f2 = f1.differentiate()
    print(f2)
    f3 = f1.integrate()
    print(f3)
    f4 = f3.integrate()
    print(f4.coeffs)
    print(f4)
