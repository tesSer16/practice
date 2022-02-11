def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root > y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root


if __name__ == "__main__":
    import sys
    read = sys.stdin.readline
    sys.setrecursionlimit(10**5)

    n, m = map(int, read().split())
    parent = [i for i in range(n)]
    answer = 0
    for i in range(m):
        v, w = map(int, read().split())
        if find(v) == find(w):
            answer = i + 1
            break
        else:
            union(v, w)

    print(answer)
