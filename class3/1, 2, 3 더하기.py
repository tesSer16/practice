import sys


dp = [1, 2, 4] + [0 for _ in range(7)]

for i in range(3, 10):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(int(input())):
    N = int(sys.stdin.readline())
    print(dp[N - 1])
