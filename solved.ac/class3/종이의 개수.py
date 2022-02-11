import sys


def check(start, end):
    initial = (lambda x, y: raw_paper[x][y])(*start)
    for a in range(start[0], end[0] + 1):
        for b in range(start[1], end[1] + 1):
            if raw_paper[a][b] != initial:
                return False

    return True


def matrixTS(n, start, end):
    if check(start, end):
        paper_cnt[(lambda x, y: raw_paper[x][y])(*start)] += 1
        return

    m = n//3
    for state in vector_tuple:
        matrixTS(m, [start[i] + m * state[i] for i in range(2)],
                 [start[i] - 1 + m * (state[i] + 1) for i in range(2)])


N = int(input())
raw_paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
vector_tuple = tuple((i, j) for i in range(3) for j in range(3))
paper_cnt = [0, 0, 0]
matrixTS(N, (0, 0), (N - 1, N - 1))
for i in [-1, 0, 1]:
    print(paper_cnt[i])
