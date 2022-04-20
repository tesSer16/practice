class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    @staticmethod
    def eye(n):
        return Matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])

    def copy(self):
        return [[self.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]

    def transpose(self):
        result = Matrix([[0] * self.rows for _ in range(self.columns)])
        for i in range(self.rows):
            for j in range(self.columns):
                result.matrix[j][i] = self.matrix[i][j]

        return result

    def is_square(self):
        return self.rows == self.columns

    def RREF(self):
        ef = Matrix(self.matrix)
        for j in range(self.rows):
            print(ef)
            for i in range(j, self.columns):
                if ef.matrix[i][j]:
                    ef.change_row(i, j)
                    for l in range(j + 1, self.columns):
                        ef.matrix[j][l] /= ef.matrix[j][j]
                    ef.matrix[j][j] = 1

                    for k in range(self.rows):
                        if k == j:
                            continue
                        for l in range(j + 1, self.columns):
                            print(ef.matrix[k][j], ef.matrix[j][j], ef.matrix[j][l])
                            ef.matrix[k][l] -= ef.matrix[k][j] / ef.matrix[j][j] * ef.matrix[j][l]
                        ef.matrix[k][j] = 0
                    break

        return ef

    def conjugate(self):
        result = Matrix(self.copy())
        for i in range(self.rows):
            for j in range(self.columns):
                result.matrix[i][j] = self.matrix[i][j].conjugate()

        return result

    def adjoint(self):
        return self.transpose().conjugate()

    def det(self):  # 개선 필요
        if self.rows == 1:
            return self.matrix[0][0]

        result = 0
        for j in range(self.columns):
            result += (-1) ** j * self.matrix[0][j] * self.cofactor(0, j).det()

        return result

    def cofactor(self, row, column):
        result = []
        for i in range(self.rows):
            if i == row:
                continue
            result.append(self.matrix[i][:column] + self.matrix[i][column + 1:])

        return Matrix(result)

    def change_row(self, r1, r2):
        self.matrix[r1], self.matrix[r2] = self.matrix[r2], self.matrix[r1]

    def scalar(self, k):
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] *= k

    def mul(self, k):
        result = Matrix(self.copy())
        for i in range(self.rows):
            for j in range(self.columns):
                result.matrix[i][j] *= k

        return result

    def scalar_row(self, row, k):
        for j in range(self.columns):
            self.matrix[row][j] *= k

    def inverse(self):
        origin = Matrix(self.copy())
        inv = Matrix.eye(self.rows)
        for j in range(self.columns):
            for i in range(j, self.columns):
                if origin.matrix[i][j]:
                    break
            else:
                return False

            origin.change_row(j, i)
            inv.change_row(j, i)

            k = origin.matrix[j][j]
            origin.scalar_row(j, 1 / k)
            inv.scalar_row(j, 1 / k)

            target_row1 = inv.matrix[j]
            target_row2 = origin.matrix[j]
            for r in range(self.rows):
                if r == j:
                    continue
                k = origin.matrix[r][j]
                for c in range(self.columns):
                    inv.matrix[r][c] -= k * target_row1[c]
                    origin.matrix[r][c] -= k * target_row2[c]

        return inv

    def trace(self):
        return sum(self.matrix[i][i] for i in range(self.rows))

    # use old determinant!
    def char_poly(self):
        pass

    def __add__(self, other):
        result = [[0] * self.columns for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return Matrix(result)

    def __sub__(self, other):
        result = [[0] * self.columns for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                result[i][j] = self.matrix[i][j] - other.matrix[i][j]

        return Matrix(result)

    def __mul__(self, other):
        result = [[0] * other.columns for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return Matrix(result)

    def __str__(self):
        print(*self.matrix, sep='\n')
        return ""


class VectorSpace:
    def __init__(self, dim, inner_product):
        self.dim = dim
        self.inner_product = inner_product

    def norm(self, vector):
        return self.inner_product(vector, vector) ** 0.5

    def gram_schmidt(self, *vectors):
        result = list(vectors)[::]
        for i in range(1, len(vectors)):
            for j in range(i):
                result[i] -= result[j].mul(
                    round(self.inner_product(vectors[i], result[j]) / self.norm(result[j])**2, 9)
                )

        return result


class Vector:
    def __init__(self, vector, vector_space):
        self.vector = vector
        self.entries = len(vector)
        self.VS = vector_space

    def conjugate(self):
        result = Vector(self.vector, self.VS)
        for i in range(self.entries):
            result.vector[i] = self.vector[i].conjugate()

        return result

    def mul(self, k):
        return Vector([k * self.vector[i] for i in range(self.entries)], self.VS)

    def __mul__(self, other):
        result = 0
        for i in range(self.entries):
            result += self.vector[i] * other.vector[i]

        return result

    def __add__(self, other):
        return Vector([self.vector[i] + other.vector[i] for i in range(self.entries)], self.VS)

    def __sub__(self, other):
        return Vector([self.vector[i] - other.vector[i] for i in range(self.entries)], self.VS)

    def __str__(self):
        return '(' + ', '.join(map(str, self.vector)) + ')'


class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs
        self.degree = len(coeffs)

    def __str__(self):
        if not self.coeffs:
            return 0

        ans = []
        for i in range(len(self.coeffs) - 1, -1, -1):
            coeff = self.coeffs[i]
            if not coeff:
                continue

            if i == 1:
                ans.append(f"{coeff}x" if coeff > 1 else "x")
            elif i == 0:
                ans.append(str(coeff))
            else:
                ans.append(f"{coeff}x^{i}" if coeff > 1 else f"x^{i}")

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

    # 해 구하기


if __name__ == "__main__":
    V = VectorSpace(4, lambda x, y: y.conjugate() * x)
    w1 = Vector([1, -2, -1, 3], V)
    w2 = Vector([3, 6, 3, -1], V)
    w3 = Vector([1, 4, 2, 8], V)
    # V = VectorSpace(4, lambda A, B: (B.adjoint() * A).trace())
    # w1 = Matrix([[2, 2], [2, 1]])
    # w2 = Matrix([[11, 4], [2, 5]])
    # w3 = Matrix([[4, -12], [3, -16]])
    # print(*V.gram_schmidt(w1, w2, w3), sep='\n')
    # f1 = Polynomial(1, 2, 1)
    # f2 = Polynomial(1, 2, 3, 4)
    # print(f1)
    # print(f2)
    # print(f1(3))
    # print(f2 - f1)
    # print(f1 * f2)
    A = Matrix([[1, 2, 3], [1, 2, 3], [5, 4, 3]])
    print(A.RREF())
