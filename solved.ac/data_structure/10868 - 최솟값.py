import sys
import math
read = sys.stdin.readline


def init():
    for i in range(N):
        sparse_table[0][i] = (i + 1 if i < N - 1 else -1, arr[i])

    for k in range(1, logn + 1):
        for i in range(N):
            a = sparse_table[k - 1][i]
            b = sparse_table[k - 1][a[0]]
            sparse_table[k][i] = (b[0], min(a[1], b[1]))


def search(a, b):
    result = min(arr[a], arr[b])
    n = b - a
    for bit in range(logn, -1, -1):
        # print(bit, a)
        if n & (1 << bit):
            result = min(result, sparse_table[bit][a][1])
            a = sparse_table[bit][a][0]

    return result


N, M = map(int, read().split())
arr = [int(read()) for _ in range(N)]
logn = int(math.log2(N))
sparse_table = [[(0, -1)] * N for _ in range(logn + 1)]
init()

# print(*sparse_table, sep='\n')
for _ in range(M):
    A, B = map(int, read().split())
    print(search(A - 1, B - 1))
