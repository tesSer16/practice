import sys
read = sys.stdin.readline


def bellman_ford(start):
    d = [INF for _ in range(N + 1)]
    d[start] = 0
    for _ in range(N - 1):
        for u, v, w in data:
            d[v] = min(d[v], d[u] + w)

    for u, v, w in data:
        if d[v] > d[u] + w:
            return False

    return True


for _ in range(int(read())):
    N, M, W = map(int, read().split())
    INF = N * 10000
    data = []
    for _ in range(M):
        S, E, T = map(int, read().split())
        data.append([S, E, T])
        data.append([E, S, T])

    for _ in range(W):
        S, E, T = map(int, read().split())
        data.append([S, E, -T])

    print("NO" if bellman_ford(1) else "YES")
