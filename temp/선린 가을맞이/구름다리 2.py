import sys
from collections import deque

N, M = map(int, input().split())
color = [''] + [1] * N
connected = [[] for _ in range(N + 1)]
for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())
    connected[v].append(w)
    connected[w].append(v)

visited = [0] * (N + 1)
q = deque([1])
while q:
    v = q.popleft()
    adj_nodes = sorted(connected[v])
    for w in adj_nodes:
        if not visited[w]:
            q.append(w)
            visited[w] = 1

    for w in adj_nodes[::-1]:
        if color[v] == color[w]:
            color[w] += 1

print(*(color[1:]), sep=' ')
