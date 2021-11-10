import sys
import heapq

N, M = map(int, input().split())
in_degree = [0] * (N + 1)
visited = [0] * (N + 1)
data = [[] for _ in range(N + 1)]
for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())
    data[v].append(w)
    in_degree[w] += 1

for datum in data:
    datum.sort()

heap = []
for v in range(1, N + 1):
    if not in_degree[v]:
        heap.append(v)

while heap:
    v = heapq.heappop(heap)
    print(v, end=' ')
    visited[v] = 1
    for w in data[v]:
        in_degree[w] -= 1
        if not in_degree[w]:
            heapq.heappush(heap, w)
