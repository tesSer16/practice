import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find(n):
    if not data[n]:
        return D[n]
    if dp[n]:
        return dp[n]

    if max_dp[n] == -1:
        max_dp[n] = max(find(m) for m in data[n])

    dp[n] = max_dp[n] + D[n]
    return dp[n]


for _ in range(int(read())):
    N, K = map(int, read().split())
    D = [0] + list(map(int, read().split()))
    data = [[] for _ in range(N + 1)]

    for _ in range(K):
        X, Y = map(int, read().split())
        data[Y].append(X)

    W = int(read())

    dp = [0] * (N + 1)
    max_dp = [-1] * (N + 1)

    print(find(W))
