import sys
import heapq
read = sys.stdin.readline

for _ in range(int(read())):
    n, k = map(int, read().split())
    a = [*map(int, read().split())]
    b = [*map(int, read().split())]
    check = [0] * n
    heap = []
    for i in range(n):
        if a[i] <= k:
            heapq.heappush(heap, -b[i])
            check[i] = 1

    while heap:
        k -= heapq.heappop(heap)
        for i in range(n):
            if not check[i] and a[i] <= k:
                heapq.heappush(heap, -b[i])
                check[i] = 1

    print(k)
