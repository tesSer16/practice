import sys
import heapq
read = sys.stdin.readline

N, K = map(int, read().split())
jewel = sorted([tuple(map(int, read().split())) for _ in range(N)], reverse=True)
bags = sorted(int(read()) for _ in range(K))

heap = []
answer = 0
for size in bags:
    while jewel and jewel[-1][0] <= size:
        heapq.heappush(heap, -jewel.pop()[1])
    if heap:
        answer -= heapq.heappop(heap)

print(answer)
