import sys
from collections import deque

N = int(input())
parent = [0] * (N + 1)
connected = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    v, w = map(int, sys.stdin.readline().split())
    connected[v].append(w)
    connected[w].append(v)


q = deque([1])
visited = [0] * (N + 1)
while q:
    v = q.popleft()
    for w in connected[v]:
        if not visited[w]:
            parent[w] = v
            q.append(w)
            visited[w] = 1

for i in range(2, N + 1):
    print(parent[i])
