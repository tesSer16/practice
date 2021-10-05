import sys

N, M = map(int, input().split())
nums = list(map(int, input().split()))
prefix = [0]
add_sum = 0
for n in nums:
    add_sum += n
    prefix.append(add_sum)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix[j] - prefix[i - 1])
