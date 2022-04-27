for _ in range(int(input())):
    K = int(input())
    pages = list(map(int, input().split()))
    dp = [[[0, 0]] * K for _ in range(K)]
    for i in range(K):
        for j in range(K - i):
            x, y = j, i + j
            dp[x][y] = [10000 * K, 0] if x != y else [pages[x], 0]
            for k in range(x, y):
                _sum = dp[x][k][0] + dp[k + 1][y][0]
                dp[x][y] = min(dp[x][y], [_sum, _sum + dp[x][k][1] + dp[k + 1][y][1]])
                # dp[x][y] = min(dp[x][y], dp[x][k] + dp[k + 1][y])

    print(dp[0][-1][1])
