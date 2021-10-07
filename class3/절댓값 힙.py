import sys
import heapq

N = int(input())
abs_heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(abs_heap, (abs(x), x))
    else:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)
