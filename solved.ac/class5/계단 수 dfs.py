def dfs(d, num, bit):
    if dp[d][num][bit]:
        return dp[d][num][bit]
    if d == N - 1:
        return 1 if bit == 1023 else 0

    temp = 0
    if num != 9:
        temp += dfs(d + 1, num + 1, bit | (1 << (num + 1)))
    if num != 0:
        temp += dfs(d + 1, num - 1, bit | (1 << (num - 1)))

    dp[d][num][bit] = temp % div
    return dp[d][num][bit]


N = int(input())
dp = [[[0] * 1024 for _ in range(10)] for _ in range(N)]
div = 10 ** 9
result = 0
for j in range(1, 10):
    result = (result + dfs(0, j, 1 << j)) % div
print(result)
