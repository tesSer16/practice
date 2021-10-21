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

    def inverse(self):
        if self.det() == 0:
            return False

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

        return result


if __name__ == "__main__":
    A = Matrix([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
    print(A.det())
