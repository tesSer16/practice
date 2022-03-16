n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

dp = [1] + [0] * k
dp[0] = 1
for a in arr:
    for j in range(a, k + 1):
        dp[j] += dp[j - a]

print(dp[k])
