N = int(input())
matrices = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
for i in range(1, N):
    for j in range(N - i):
        x, y = j, i + j
        dp[x][y] = 2 ** 32
        for k in range(x, y):
            l, m, r = matrices[x], matrices[k], matrices[y]
            dp[x][y] = min(dp[x][y], dp[x][k] + dp[k + 1][y] + l[0] * m[1] * r[1])

print(dp[0][-1])
