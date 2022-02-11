import sys
from collections import Counter

N, M, B = map(int, input().split())
blocks = []

for _ in range(N):
    blocks += list(map(int, sys.stdin.readline().split()))

height_list = Counter(blocks)
sum_block = sum(blocks) + B

min_time = (256 * M * N, 0)
for i in range(sum_block // (N * M) + 1):
    time = 0
    for j in range(257):
        if j > i:
            time += (j - i) * 2 * height_list[j]
        elif j <= i:
            time += (i - j) * height_list[j]

    if min_time[0] >= time:
        min_time = (time, i)

print(*min_time)
