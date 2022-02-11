import sys

N = int(input())
INF = float('inf')
dp = [[[0, 0] for _ in range(3)] for _ in range(2)]

idx = 0
for _ in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(3):
        dp[idx][j][0] = dp[idx][j][1] = data[j]
        dp[idx][j][0] += min([dp[idx ^ 1][k][0] if 0 <= k <= 2 else INF for k in range(j - 1, j + 2)])
        dp[idx][j][1] += max([dp[idx ^ 1][k][1] if 0 <= k <= 2 else -INF for k in range(j - 1, j + 2)])
    idx ^= 1

result = list(zip(*dp[(N % 2) ^ 1]))
print(max(result[1]), min(result[0]))
