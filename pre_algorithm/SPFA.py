from collections import deque


def SPFA(start):
    d = [INF for _ in range(N + 1)]
    in_que = [0 for _ in range(N + 1)]
    cycled = [0 for _ in range(N + 1)]
    d[start] = 0
    in_que[start] = 1
    q = deque([start])
    while q:
        u = q.popleft()
        in_que[u] = 0
        for v, w in data[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                if not in_que[v]:
                    cycled[v] += 1
                    if cycled[v] >= N:
                        return False

                    in_que[v] = 1
                    q.append(v)

    return d


N, M, W = 3, 2, 1
data = [[],
        [(2, 3)],
        [(1, 3), (3, 4)],
        [(2, 4), (1, -8)]]

INF = 10000 * N
print(SPFA(1))
