import sys
read = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return rank[root_x]

    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
        rank[root_x] += rank[root_y]
    elif rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
        rank[root_y] += rank[root_x]
    else:
        parent[root_y] = root_x
        rank[root_x] += rank[root_y]

    return max(rank[root_x], rank[root_y])


for _ in range(int(read())):
    N = int(read())
    rank = [1] * 2 * N
    parent = [i for i in range(2 * N)]

    data = {}
    num = 0
    for _ in range(N):
        A, B = read().strip().split()
        if A not in data:
            data[A] = num
            num += 1
        if B not in data:
            data[B] = num
            num += 1

        print(union(data[A], data[B]))
