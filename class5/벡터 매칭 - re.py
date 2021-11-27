from itertools import combinations
import sys
read = sys.stdin.readline


def cal(x, y):
    return ((2 * sum(x) - sum_x)**2 + (2 * sum(y) - sum_y)**2)**0.5


for _ in range(int(read())):
    N = int(read())
    data = [list(map(int, read().split())) for _ in range(N)]
    sum_x, sum_y = (lambda x: (sum(x[0]), sum(x[1])))(list(zip(*data)))
    answer = float('inf')
    print(min([cal(*zip(*case)) for case in combinations(data, N // 2)]))
