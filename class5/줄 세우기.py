import sys
from collections import deque

N, M = map(int, input().split())
in_degree = [0] * (N + 1)
data = [[0] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    data[A].append(B)
    in_degree[B] += 1

q = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        q.append(i)

result = []
while q:
    v = q.popleft()
    result.append(v)
    for w in data[v]:
        in_degree[w] -= 1
        if in_degree[w] == 0:
            q.append(w)

print(*result)
