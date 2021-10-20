N = 1000000
dp = [[0, 0] for _ in range(N)]
dp[0][0], dp[0][1] = 3, 4
for i in range(1, N):
    dp[i][0] = (3 * dp[i - 1][0] + dp[i - 1][1]) % 1000000007
    dp[i][1] = (4 * dp[i - 1][0] + 2 * dp[i - 1][1]) % 1000000007

for _ in range(int(input())):
    idx = int(input()) - 1
    print(sum(dp[idx]) % 1000000007)
