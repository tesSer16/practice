from itertools import permutations

N, M = map(int, input().split())
for per in permutations(sorted(map(int, input().split())), M):
    print(*per, sep=' ')
