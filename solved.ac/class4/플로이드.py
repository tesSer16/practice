import sys

N = int(input())
M = int(input())

INF = 100000 * N
result = [[0 if i == j else INF for j in range(N)] for i in range(N)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    result[a - 1][b - 1] = min(result[a - 1][b - 1], c)

for k in range(N):
    for i in range(N):
        for j in range(N):
            result[i][j] = min(result[i][j], result[i][k] + result[k][j])

for res in result:
    for r in res:
        if r >= INF:
            print(0, end=" ")
        else:
            print(r, end=" ")
    print()
