def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(rx, ry):
    x_root = find(rx)
    y_root = find(ry)

    if x_root == y_root:
        return

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        parent[y_root] = x_root
        if rank[x_root] == rank[y_root]:
            rank[x_root] += 1


N, M = map(int, input().split())
rank = [0] * (M * N)
parent = [p for p in range(M * N)]
board = [input() for _ in range(N)]
directions = {'D': (1, 0), 'L': (0, -1), 'R': (0, 1), 'U': (-1, 0)}
for x in range(N):
    for y in range(M):
        dx, dy = directions[board[x][y]]
        nx, ny = x + dx, y + dy
        union(M * x + y, M * nx + ny)

print(len(set(find(i) for i in range(M * N))))
