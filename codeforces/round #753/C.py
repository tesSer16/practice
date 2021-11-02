import sys

for _ in range(int(input())):
    n = int(sys.stdin.readline())
    num_list = sorted(list(map(int, sys.stdin.readline().split())))
    prefix = num_list[::]
    _sum = num_list[0]
    for i in range(1, n):
        prefix[i] -= _sum
        _sum += prefix[i]

    print(max(prefix))
