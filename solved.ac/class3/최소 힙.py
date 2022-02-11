import sys
import heapq

N = int(input())
min_heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(min_heap, x)
    else:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)
