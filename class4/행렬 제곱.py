def R2L(g, k):
    if g == 0:
        return 0

    A, B = [[1 if i == j else 0 for j in range(n)] for i in range(n)], g
    k = format(k, 'b')

    for ki in k[::-1]:
        if ki == '1':
            A = matrix_product(A, B)
        B = matrix_product(B, B)

    return A


def matrix_product(A, B):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (A[i][k] * B[k][j]) % 1000

    return result


n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = R2L(matrix, b)
for ans in answer:
    for a in ans:
        print(a % 1000, end=" ")
    print()
