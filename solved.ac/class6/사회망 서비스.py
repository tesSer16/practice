import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(v, w):
    if len(data[w]) == 1:
        check[v] = 1
        return

    for z in data[w]:
        if z == v:
            continue

        dfs(w, z)
    if not check[w]:
        check[v] = 1


N = int(read())
data = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, read().split())
    data[a].append(b)
    data[b].append(a)

check = [0] * (N + 1)
for u in data[1]:
    dfs(1, u)
    if not check[u]:
        check[1] = 1

print(sum(check))
