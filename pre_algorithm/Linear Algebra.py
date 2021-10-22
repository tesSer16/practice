class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    @staticmethod
    def eye(n):
        return Matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])

    def det(self):
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

    def scalar_row(self, row, k):
        for j in range(self.columns):
            self.matrix[row][j] *= k

    def inverse(self):
        origin = Matrix(self.matrix)
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

    def __add__(self, other):
        # return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)])
        result = [[0] * self.columns for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return Matrix(result)

    def __mul__(self, other):
        result = [[0] * other.columns for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result[i][j] += self.matrix[i][k] * self.matrix[k][j]

        return Matrix(result)


if __name__ == "__main__":
    A = Matrix([[5, 8, -4],
                [6, 9, -5],
                [4, 7, -2]])
    inv_A = A.inverse()
    print(*inv_A.matrix, sep='\n')
