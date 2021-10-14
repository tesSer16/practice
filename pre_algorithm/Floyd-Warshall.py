import sys

N, M = map(int, input().split())
result = [[0 if i == j else N for j in range(N)] for i in range(N)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    result[x - 1][y - 1] = result[y - 1][x - 1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            result[i][j] = min(result[i][j], result[i][k] + result[k][j])

print(*result, sep='\n')
