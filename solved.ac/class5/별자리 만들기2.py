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


N = int(input())
stars = []
data = []
for i in range(N):
    x1, y1 = map(float, input().split())
    for j in range(len(stars)):
        x2, y2 = stars[j]
        dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        data.append((dist, i, j))

    stars.append((x1, y1))

data.sort(reverse=True)
parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)

total_w = edges = 0
while edges < N - 1:
    C, A, B = data.pop()
    if find(A) == find(B):
        continue

    union(A, B)
    total_w += C
    edges += 1

print(total_w)
