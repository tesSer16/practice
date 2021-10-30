import sys
import heapq

V, E = map(int, input().split())
data = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    data[A].append([B, C])
    data[B].append([A, C])

tree = [0] * (V + 1)
tree[1] = 1
heap = []
for b, c in data[1]:
    heapq.heappush(heap, (c, b))

total_w = 0
while heap:
    C, B = heapq.heappop(heap)
    if not tree[B]:
        total_w += C
        tree[B] = 1
        for b, c in data[B]:
            heapq.heappush(heap, (c, b))

print(total_w)
