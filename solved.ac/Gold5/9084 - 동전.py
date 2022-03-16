for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())

    dp = [1] + [0] * k
    dp[0] = 1
    for a in arr:
        for j in range(a, k + 1):
            dp[j] += dp[j - a]

    print(dp[k])
