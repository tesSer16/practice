import sys


def find(x):
    if parent[x] == x:
        return x
    else:
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


V, E = map(int, input().split())
parent = [i for i in range(V + 1)]
rank = [0] * (V + 1)
data = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(E)], key=lambda x: -x[2])
total_w = edges = 0
while edges < V - 1:
    A, B, C = data.pop()
    if find(A) == find(B):
        continue

    union(A, B)
    total_w += C
    edges += 1

print(total_w)
