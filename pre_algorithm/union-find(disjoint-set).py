# BOJ 1717

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return

    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    elif rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


N, M = map(int, input().split())
rank = [0] * (N + 1)
parent = [i for i in range(N + 1)]
for _ in range(M):
    s, a, b = map(int, input().split())
    if s:
        print(["NO", "YES"][find(a) == find(b)])
    else:
        union(a, b)
