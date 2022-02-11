import sys


def check(start, end):
    initial = (lambda x, y: law_paper[x][y])(*start)
    for a in range(start[0], end[0] + 1):
        for b in range(start[1], end[1] + 1):
            if law_paper[a][b] != initial:
                return False

    return True


def matrixBS(start, end):
    if check(start, end):
        wb_cnt[(lambda x, y: law_paper[x][y])(*start)] += 1
        return

    middle = [(s + e) // 2 for s, e in zip(start, end)]
    for state in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        matrixBS([start[i] + (end[i] - middle[i]) * state[i] for i in range(2)],
                 [middle[i] + (end[i] - middle[i]) * state[i] for i in range(2)])


N = int(input())
law_paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

wb_cnt = [0, 0]
matrixBS((0, 0), (N - 1, N - 1))
print(wb_cnt[0])
print(wb_cnt[1])
