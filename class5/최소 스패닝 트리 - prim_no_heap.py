import sys

V, E = map(int, input().split())
data = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    data[A].append([B, C])
    data[B].append([A, C])

INF = float('inf')
tree = [0] * (V + 1)
dist = [INF] * (V + 1)
dist[1] = 0
total_w = 0

for u in range(V + 1):
    now, min_dist = -1, INF
    for v in range(V + 1):
        if not tree[v] and min_dist > dist[v]:
            min_dist = dist[v]
            now = v
    if now < 0:
        break

    total_w += min_dist
    tree[now] = 1
    for b, c in data[now]:
        dist[b] = min(dist[b], c)

print(total_w)
