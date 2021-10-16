def comb(k, r):
    if dp[k][r]:
        return dp[k][r]
    dp[k][r] = comb(k - 1, r - 1) + comb(k - 1, r)
    return dp[k][r]


n, m = map(int, input().split())
dp = [[1 if i == j or j == 0 else 0 for j in range(i + 1)] for i in range(n + 1)]
print(comb(n, m))
