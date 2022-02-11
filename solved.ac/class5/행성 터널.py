import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        parent[y_root] = x_root
        if rank[x_root] == rank[y_root]:
            rank[x_root] += 1


V = int(input())
parent = [i for i in range(V)]
rank = [0] * V
planets = [tuple(map(int, sys.stdin.readline().split())) for _ in range(V)]
data = [sorted([(i, v[k]) for i, v in enumerate(planets)], key=lambda x: x[1]) for k in range(3)]
edges = sorted([(abs(pk[i][1] - pk[i + 1][1]), pk[i][0], pk[i + 1][0]) for i in range(V - 1) for pk in data], reverse=True)

total_w = E = 0
while E < V - 1:
    w, u, v = edges.pop()
    if find(u) == find(v):
        continue

    union(u, v)
    total_w += w
    E += 1

print(total_w)
