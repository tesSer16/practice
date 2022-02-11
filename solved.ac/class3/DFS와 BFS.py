import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
connected = {i: [] for i in range(N + 1)}
for _ in range(M):
    v1, v2 = map(int, input().split())
    connected[v1].append(v2)
    connected[v2].append(v1)

bfs_result = []


def dfs(v, dfs_result=None):
    if dfs_result is None:
        dfs_result = []

    dfs_result.append(v)
    print(v, end=' ')

    for w in sorted(connected[v]):
        if w not in dfs_result:
            dfs(w, dfs_result)


def bfs(v):
    q = deque()
    q.append(v)
    bfs_result.append(v)

    while q:
        current_v = q.popleft()
        print(current_v, end=' ')

        for w in sorted(connected[current_v]):
            if w not in bfs_result:
                bfs_result.append(w)
                q.append(w)


dfs(V)
print()
bfs(V)
