def dfs(d, c, k):
    if dp[c][k] < INF:
        return dp[c][k]
    if d == n - 1:
        return m[c][0] if m[c][0] else INF

    for i in range(n):
        nk = k | 1 << i
        if k != nk and m[c][i]:
            dp[c][k] = min(dp[c][k], dfs(d + 1, i, nk) + m[c][i])

    return dp[c][k]


n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
INF = float('inf')
dp = [[INF] * (1 << n) for _ in range(n)]
dfs(0, 0, 1)
print(dp[0][1])
