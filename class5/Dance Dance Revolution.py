*num_list, dum = map(int, input().split())
N = len(num_list)
INF = float('inf')
dp = [{k: INF for k in [12, 13, 14, 23, 24, 34, 10, 20, 30, 40]} for _ in range(N)]

dp[0][num_list[0] * 10] = 2

for i in range(1, N):
    num = num_list[i]
    for k, v in dp[i - 1].items():
        if v >= float('inf'):
            continue

        a, b = k // 10, k % 10
        if a == num or b == num:
            dp[i][k] = min(dp[i][k], v + 1)
        elif b == 0:
            add = 3 if (a + num) % 2 else 4
            dp[i][num * 10] = min(dp[i][num * 10], v + add)
            key = 10 * min(a, num) + max(a, num)
            dp[i][key] = min(dp[i][key], v + 2)
        else:
            for c, d in ((a, b), (b, a)):
                add = 3 if (c + num) % 2 else 4
                key = 10 * min(d, num) + max(d, num)
                dp[i][key] = min(dp[i][key], v + add)

print(min(dp[-1].values()))
