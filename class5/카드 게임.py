import bisect


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
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root
        if rank[x_root] == rank[y_root]:
            rank[y_root] += 1


N, M, K = map(int, input().split())
rank = [0] * N
parent = [0] * N
card_pool = sorted(list(map(int, input().split())))
battle = list(map(int, input().split()))

for b in battle:
    v = bisect.bisect_right(card_pool, b)
    print(find(v))
    if v < M - 1:
        union(v, v + 1)
    else:
        union(v, v - 1)
