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
                result[i] -= result[j].mul(round(self.inner_product(vectors[i], result[j]) / self.norm(result[j])**2, 9))

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
    pass


class Scalar:
    pass


if __name__ == "__main__":
    # V = VectorSpace(4, lambda x, y: y.conjugate() * x)
    # w1 = Vector([1, -2, -1, 3], V)
    # w2 = Vector([3, 6, 3, -1], V)
    # w3 = Vector([1, 4, 2, 8], V)
    V = VectorSpace(4, lambda A, B: (B.adjoint() * A).trace())
    w1 = Matrix([[3, 5], [-1, 1]])
    w2 = Matrix([[-1, 9], [5, -1]])
    w3 = Matrix([[7, -17], [2, -6]])
    print(*V.gram_schmidt(w1, w2, w3), sep='\n')
