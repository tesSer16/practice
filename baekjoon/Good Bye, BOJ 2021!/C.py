import sys
read = sys.stdin.readline

N, G, K = map(int, read().split())
A, B = [], []
for _ in range(N):
    s, l, o = map(int, read().split())
    B.append((l, s)) if o else A.append((l, s))

start, end = 0, 2 * 10 ** 9 + 1
while start + 1 < end:
    mid = (start + end) // 2
    germ = sum([s * max(1, mid - l) for l, s in A])
    germ += sum(sorted([s * max(1, mid - l) for l, s in B], reverse=True)[K:])
    if germ <= G:
        start = mid
    else:
        end = mid
print(start)
