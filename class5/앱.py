N, M = map(int, input().split())
mem = [*map(int, input().split())]
cost = [*map(int, input().split())]
_sum = sum(cost)

dp = [0] * (_sum + 1)
for i in range(N):
    for j in range(_sum, cost[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - cost[i]] + mem[i])

for j in range(_sum + 1):
    if dp[j] >= M:
        print(j)
        break
