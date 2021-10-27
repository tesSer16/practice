import heapq

input()
temp = list(map(int, input().split()))
max_heap = []
for i, t in enumerate(temp):
    heapq.heappush(max_heap, (-t, i, 1))

min_cake = -max(max_heap, key=lambda x: x[0])[0]
min_diff = -max_heap[0][0] - min_cake
for _ in range(int(input())):
    cake, idx, cnt = heapq.heappop(max_heap)
    piece = temp[idx] / (cnt + 1)
    min_cake = min(min_cake, piece)

    heapq.heappush(max_heap, (-piece, idx, cnt + 1))

    min_diff = min(min_diff, -max_heap[0][0] - min_cake)

print(min_diff)
