import heapq
import sys
read = sys.stdin.readline

N = int(read())
heap1 = []
heap2 = [int(read())]
print(heap2[0])
for _ in range(N - 1):
    x = int(read())
    if len(heap1) == len(heap2):
        if -heap1[0] < x:
            heapq.heappush(heap2, x)
        else:
            heapq.heappush(heap2, -heapq.heappop(heap1))
            heapq.heappush(heap1, -x)
        print(heap2[0])
    else:
        if heap2[0] > x:
            heapq.heappush(heap1, -x)
        else:
            heapq.heappush(heap1, -heapq.heappop(heap2))
            heapq.heappush(heap2, x)
        print(-heap1[0])
