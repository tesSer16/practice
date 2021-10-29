import sys
import heapq

V, E = map(int, input().split())
connected = [0] * (V + 1)
heap = []
total_w = 0
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    connected[A] += 1
    connected[B] += 1
    heapq.heappush(heap, (-C, A, B))
    total_w += C

while E > V - 1:
    C, A, B = heapq.heappop(heap)
    if connected[A] > 1 and connected[B] > 1:
        connected[A] -= 1
        connected[B] -= 1
        total_w += C
        E -= 1

print(total_w)
