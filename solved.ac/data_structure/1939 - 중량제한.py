import heapq
import sys
read = sys.stdin.readline

N, M = map(int, read().split())
data = [[(0, -1)] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, read().split())
    data[A].append((B, C))
    data[B].append((A, C))

start, end = map(int, read().split())
heap = [(-10 ** 9, start)]
answer = 10 ** 9
visited = [0] * (N + 1)
while heap:
    w, c = heapq.heappop(heap)
    visited[c] = 1
    answer = min(answer, -w)
    if c == end:
        break

    for nc, nw in data[c]:
        if not nc or visited[nc]:
            continue
        heapq.heappush(heap, (-nw, nc))

print(answer)
