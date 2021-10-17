import sys

for _ in range(int(input())):
    N = int(sys.stdin.readline())
    dp = [[0 for _ in range(N)], [0 for _ in range(N)]]
    dp[0][0], dp[1][0] = 3, 4
    for i in range(1, N):
        temp = ((dp[0][i - 1] << 2) + (dp[1][i - 1] << 1)) % 1000000007
        dp[1][i] += temp
        dp[0][i] += (dp[0][i - 1] + (temp >> 1)) % 1000000007

    print((dp[0][-1] + dp[1][-1]) % 1000000007)
