string = input()
n = len(string)

dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n - i):
        if string[j:j + i + 1] == string[j + i:j:-1] + string[j]:
            dp[j][j + i] = 1
        else:
            dp[j][j + i] = min(dp[j][j + k] + dp[j + 1 + k][j + i] for k in range(i))

print(*dp, sep='\n')
print(dp[0][n - 1])
