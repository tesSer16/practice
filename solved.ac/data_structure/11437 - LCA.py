import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)


def init(u, v, d):
    global max_depth
    for w in data[v]:
        if w != u:
            init(v, w, d + 1)

    parent[v] = u
    depth[v] = d
    max_depth = max(d, max_depth)


N = int(read())
data = [[] for _ in range(N + 1)]
depth = [0] * (N + 1)
parent = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, read().split())
    data[a].append(b)
    data[b].append(a)

max_depth = 0
init(0, 1, 1)
log_d = 0
while 1 << (log_d + 1) < max_depth:
    log_d += 1

sparse_arr = [parent] + [[0] * (N + 1) for _ in range(log_d)]
for i in range(1, log_d + 1):
    for j in range(1, N + 1):
        sparse_arr[i][j] = sparse_arr[i - 1][sparse_arr[i - 1][j]]

# print(*sparse_arr, sep='\n')

for _ in range(int(read())):
    A, B = map(int, read().split())
    if depth[B] > depth[A]:
        A, B = B, A

    k = log_d
    while depth[A] != depth[B]:
        for i in range(k, -1, -1):
            if sparse_arr[i][A] == 0:
                k -= 1
                continue

            if depth[B] <= depth[A] - (1 << i):
                A = sparse_arr[i][A]
                break

    lca = A
    if A == B:
        print(lca)
        continue

    for i in range(k, -1, -1):
        if sparse_arr[i][A] != sparse_arr[i][B]:
            A = sparse_arr[i][A]
            B = sparse_arr[i][B]
        lca = sparse_arr[i][A]

    print(lca)
