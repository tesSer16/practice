import heapq

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
heap = []
for i, bi in enumerate(b):
    if a[i] != 100:
        heapq.heappush(heap, (-bi, i))

N *= 24
while N and heap:
    score, sub = heapq.heappop(heap)
    # print(score, sub, a)
    current = a[sub]
    temp = (100 - a[sub]) // (-score)
    if N >= temp:
        N -= temp
        a[sub] += temp * (-score)
    else:
        a[sub] += N * (-score)
        N = 0

    if a[sub] != 100:
        heapq.heappush(heap, (-(100 - a[sub]), sub))

# print(a)
print(sum(a))
