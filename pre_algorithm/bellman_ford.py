def bellman_ford(start):
    d = [INF for _ in range(N + 1)]
    d[start] = 0
    for _ in range(N - 1):
        for u, v, w in data:
            d[v] = min(d[v], d[u] + w)

    for u, v, w in data:
        if d[v] > d[u] + w:
            return False

    return d


N, M = 3, 4
data = [(1, 2, 2), (2, 1, 2),
        (1, 3, 4), (3, 1, 4),
        (2, 3, 1), (3, 2, 1),
        (3, 1, 3)]

INF = N * 10000

print(bellman_ford(1))
