import sys
import heapq
read = sys.stdin.readline


n = int(read())
data = []
for _ in range(n):
    h, o = map(int, read().split())
    if h > o:
        h, o = o, h

    data.append((h, o))
data.sort(key=lambda x: x[1])
d = int(read())

heap = []
answer = 0
for h, o in data:
    if o - h <= d:
        heapq.heappush(heap, h)

    while heap and o - heap[0] > d:
        heapq.heappop(heap)
    answer = max(answer, len(heap))
print(answer)
