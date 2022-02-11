import sys
sys.setrecursionlimit(10**5)


def dfs(v):
    visited[v] = 1
    for w in graph[v]:
        if not visited[w]:
            dfs(w)


N, M = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
