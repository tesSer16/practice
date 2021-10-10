import sys

N, M, B = map(int, input().split())
blocks = []
total_blocks = B
min_num = 256
for _ in ' ' * N:
    temp = list(map(int, sys.stdin.readline().split()))
    min_num = min(min_num, min(temp))
    total_blocks += sum(temp)
    blocks.append(temp)

ini_k = total_blocks // (N * M)
min_time = 512 * N * M
max_k = 0

for k in range(min_num, ini_k + 1):
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
