def find(x):
    if x != root[x]:
        root[x] = find(x)
    return root[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        if rank[root_x] > root_y[root_y]:
            root[root_y] = root_x
        elif rank[root_y] > rank[root_x]:
            root[root_x] = root_y
        else:
            root[root_y] = root_x
            rank[root_x] += 1


N = 10
root = [i for i in range(N)]
rank = [0 for _ in range(N)]
