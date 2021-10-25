import sys
from collections import deque
read = sys.stdin.readline


for _ in range(int(read())):
    N, K = map(int, read().split())
    D = [0] + list(map(int, read().split()))
    data = [[] for _ in range(N + 1)]
    in_deg = [0] * (N + 1)
    dp = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, read().split())
        data[X].append(Y)
        in_deg[Y] += 1

    q = deque([0])
    for v in range(1, N + 1):
        if in_deg[v] == 0:
            q.append(v)
            dp[v] = D[v]

    while q:
        v = q.popleft()
        for w in data[v]:
            in_deg[w] -= 1
            dp[w] = max(dp[v] + D[w], dp[w])
            if in_deg[w] == 0:
                q.append(w)

    W = int(read())
    print(dp[W])
