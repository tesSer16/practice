for _ in range(int(input())):
    n = int(input())
    s = [list(map(int, input().split())), list(map(int, input().split()))]
    if n == 1:
        print(max(s[0][0], s[1][0]))
        continue

    dp = [[0 for _ in range(n)] for _ in '  ']
    dp[0][0], dp[1][0] = s[0][0], s[1][0]
    dp[0][1], dp[1][1] = s[1][0] + s[0][1], s[0][0] + s[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[0][i - 2], dp[1][i - 2], dp[1][i - 1]) + s[0][i]
        dp[1][i] = max(dp[0][i - 2], dp[1][i - 2], dp[0][i - 1]) + s[1][i]

    print(max(dp[0][n - 1], dp[1][n - 1]))
