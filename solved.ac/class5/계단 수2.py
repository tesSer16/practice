N = int(input())
dp = [[[0] * 1024 for _ in range(10)] for _ in range(N)]
div = 10 ** 9

for j in range(1, 10):
    dp[0][j][1 << j] = 1

for i in range(1, N):
    for j in range(10):
        for k in range(1024):
            if j != 9:
                dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i - 1][j + 1][k]) % div
            if j != 0:
                dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i - 1][j - 1][k]) % div

result = 0
for j in range(10):
    result = (result + dp[N - 1][j][1023]) % div

print(result)
