import sys
from collections import deque

read = sys.stdin.readline


def dfs(u):
    if visited[u]:
        return False

    visited[u] = 1
    for v, w in data[u]:
        dfs(v)

    return True


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

    return True


def check(_list):
    for node in _list:
        if not SPFA(node):
            return False

    return True


for _ in range(int(read())):
    N, M, W = map(int, read().split())
    INF = N * 10000 + 1
    data = [[] for _ in range(N + 1)]
    for _ in range(M):
        S, E, T = map(int, read().split())
        data[S].append([E, T])
        data[E].append([S, T])

    for _ in range(W):
        S, E, T = map(int, read().split())
        data[S].append([E, -T])

    visited = [0] * (N + 1)
    candidates = []
    for i in range(1, N + 1):
        if dfs(i):
            candidates.append(i)

    print("NO" if check(candidates) else "YES")
