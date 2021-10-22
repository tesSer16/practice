import sys


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    @staticmethod
    def eye(n):
        return Matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])

    def change_row(self, r1, r2):
        self.matrix[r1], self.matrix[r2] = self.matrix[r2], self.matrix[r1]

    def scalar_row(self, row, k):
        for j in range(self.columns):
            self.matrix[row][j] /= k

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
            origin.scalar_row(j, k)
            inv.scalar_row(j, k)

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


N = int(input())
A = Matrix([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
inv_A = A.inverse()
if inv_A:
    for line in inv_A.matrix:
        print(*line, sep=" ")
else:
    print("no inverse")
