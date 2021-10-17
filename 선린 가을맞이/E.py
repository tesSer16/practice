import sys

N, M = map(int, input().split())
color = [''] + [1] * N
connected = [[] for _ in range(N + 1)]
for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())
    connected[v].append(w)
    connected[w].append(v)

for v in range(1, N + 1):
    for w in connected[v]:
        if color[v] == color[w]:
            color[w] += 1

print(*(color[1:]), sep=' ')
