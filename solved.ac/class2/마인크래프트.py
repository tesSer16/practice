import sys

N, M, B = map(int, input().split())
blocks = [list(map(int, sys.stdin.readline().split())) for _ in ' ' * N]
min_time = 512 * N * M
max_k = 0

for k in range(257):
    time, rest_block = 0, B
    for i in range(N):
        for j in range(M):
            value = blocks[i][j] - k
            if value > 0:
                time += value * 2
            else:
                time += (-value)
            rest_block += value

    if rest_block >= 0 and time <= min_time:
        min_time = time
        max_k = k

print(min_time, max_k)
