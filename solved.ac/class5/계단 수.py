N = int(input())
if N <= 9:
    print(0)
else:
    dp = [[[0] * 10 for _ in range(10)] for _ in range(N)]
    dp[9][9][0] = 1
    dp[10][8][0] = 1
    dp[10][9][1] = 1
    for i in range(9, N - 2):
        for x in range(1, 10):
            for y in range(10):
                val = dp[i][x][y]
                if not val:
                    continue

                dp[i + 2][x][y] += i * val
                for d in [-2, 0, 2]:
                    if 0 < x + d <= 9 and not (d == 0 and x == 9):
                        dp[i + 2][x + d][y] += val
                    if 0 <= y + d <= 9 and not ((y == 0 or y == 9) and d == 0):
                        dp[i + 2][x][y + d] += val

    _sum = 0
    print(*dp[N - 2], sep='\n')
    print(*dp[N - 1], sep='\n')
    for k in range(9, N):
        _sum += sum(sum(dn) for dn in dp[k])
    print(sum(sum(dn) for dn in dp[N - 1]))
    print(_sum)
