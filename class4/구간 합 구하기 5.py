import sys

read = sys.stdin.readline

N, M = map(int, read().split())
matrix = [[0] * (N + 1)] + [[0] + list(map(int, read().split())) for _ in range(N)]
prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
for k in range(1, N + 1):
    for i in range(k, N + 1):
        prefix_sum[i][k] = prefix_sum[i][k - 1] + prefix_sum[i - 1][k] - \
                           prefix_sum[i - 1][k - 1] + matrix[i][k]

        prefix_sum[k][i] = prefix_sum[k - 1][i] + prefix_sum[k][i - 1] - \
                           prefix_sum[k - 1][i - 1] + matrix[k][i]

for _ in range(M):
    x1, y1, x2, y2 = map(int, read().split())
    print(prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] +
          prefix_sum[x1 - 1][y1 - 1])
