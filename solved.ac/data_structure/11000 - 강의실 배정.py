import sys
import heapq
read = sys.stdin.readline

N = int(read())
data = sorted([tuple(map(int, read().split())) for _ in range(N)])
num = 1
end = [data[0][0]]
for s, t in data:
    if s < end[0]:
        num += 1
    else:
        heapq.heappop(end)
    heapq.heappush(end, t)

print(num)
