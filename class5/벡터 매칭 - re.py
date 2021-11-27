from itertools import combinations
import sys
read = sys.stdin.readline

for _ in range(int(read())):
    N = int(read())
    data = [list(map(int, read().split())) for _ in range(N)]
    sum_x, sum_y = (lambda x: (sum(x[0]), sum(x[1])))(list(zip(*data)))
    answer = float('inf')

    for case in combinations(data, N // 2):
        x1, y1 = (lambda x: (sum(x[0]), sum(x[1])))(list(zip(*case)))
        answer = min(answer, ((2 * x1 - sum_x)**2 + (2 * y1 - sum_y)**2)**0.5)

    print(answer)
