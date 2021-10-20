N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

dp = [[[var, var] for var in datum] for datum in data]
INF = float('inf')

for i in range(1, N):
    for j in range(3):
        dp[i][j][0] += min([dp[i - 1][k][0] if 0 <= k <= 2 else INF for k in range(j - 1, j + 2)])
        dp[i][j][1] += max([dp[i - 1][k][1] if 0 <= k <= 2 else -INF for k in range(j - 1, j + 2)])

result = list(zip(*dp[-1]))
print(max(result[1]), min(result[0]))
