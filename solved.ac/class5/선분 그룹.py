import sys
read = sys.stdin.readline


def solution(x1, y1, x2, y2, x3, y3, x4, y4):
    def check(r1, r2, target):
        r = sorted([r1, r2])
        return r[0] <= target <= r[1]

    a, b, c, d, e, f = y4 - y3, x3 - x4, y2 - y1, x1 - x2, (y4 - y3) * x3 - y3 * (x4 - x3), (y2 - y1) * x1 - y1 * (
            x2 - x1)
    det = a * d - b * c
    x, y = d * e - b * f, a * f - e * c

    if det == 0:
        if a == b == 0:
            if c * (x3 - x1) == - d * (y3 - y1) and all(check(r, s, t) for r, s, t in [(x1, x2, x3), (y1, y2, y3)]):
                return 1
        elif c == d == 0:
            if a * (x1 - x3) == - b * (y1 - y3) and all(check(r, s, t) for r, s, t in [(x3, x4, x1), (y3, y4, y1)]):
                return 1

        elif a * (x3 - x1) == - b * (y3 - y1):
            if x1 == x3:
                x1, x2, x3, x4 = y1, y2, y3, y4
            t1, t2 = sorted([x1, x2])
            t3, t4 = sorted([x3, x4])
            if (t1 <= t3 <= t2) or (t1 <= t4 <= t2) or (t3 <= t2 <= t4) or (t3 <= t1 <= t4):
                return 1

    elif all(check(r * det, s * det, t) for r, s, t in [(x1, x2, x), (x3, x4, x), (y1, y2, y), (y3, y4, y)]):
        return 1

    return 0


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


N = int(read())
parent = list(range(N))
rank = [0] * N
lines = [tuple(map(int, read().split()))]
for j in range(1, N):
    line = tuple(map(int, read().split()))
    for i in range(len(lines)):
        if solution(*lines[i], *line):
            union(i, j)

    lines.append(line)

disjoint_set = {}
for i in range(N):
    parent[i] = find(i)
    disjoint_set[parent[i]] = disjoint_set.get(parent[i], 0) + 1

print(len(disjoint_set))
print(max(disjoint_set.values()))
