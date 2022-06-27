import heapq
import sys
read = sys.stdin.readline

N = int(read())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(read()))
result = 0
for _ in range(N - 1):
    val = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, val)

    result += val
    print(heap)

print(result)
