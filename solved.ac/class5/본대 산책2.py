def R2L(g, k):
    A, B = [[1 if i == j else 0 for j in range(8)] for i in range(8)], g
    for ki in format(k, 'b')[::-1]:
        if ki == '1':
            A = product(A, B)
        B = product(B, B)

    return A[0][0] % div


def product(m1, m2):
    result = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                result[i][j] += (m1[i][k] * m2[k][j]) % div

    return result


div = 1_000_000_007
matrix = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 0, 0, 0],
          [1, 1, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 0],
          [0, 0, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 1, 1, 0, 1, 0],
          [0, 0, 0, 0, 0, 1, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0]]

print(R2L(matrix, int(input())))
