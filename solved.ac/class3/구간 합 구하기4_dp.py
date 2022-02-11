import sys


def dp_sum(i, j):
    if dp[i][j]:
        return dp[i][j]
    else:
        right_sum = dp_sum(i + 1, j)
        left_sum = dp_sum(i, j - 1)
        dp[i][j] = dp[i][i] + right_sum
        return dp[i][j]


N, M = map(int, input().split())
nums = list(map(int, input().split()))
dp = [[nums[i] if i == j else 0 for j in range(N)] for i in range(N)]

for _ in range(M):
    i, j = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    print(dp_sum(i, j))
