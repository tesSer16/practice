import sys


def check(start, end):
    initial = (lambda x, y: screen[x][y])(*start)
    for a in range(start[0], end[0] + 1):
        for b in range(start[1], end[1] + 1):
            if screen[a][b] != initial:
                return False

    return True


def matrixBS(start, end):
    if check(start, end):
        print((lambda x, y: screen[x][y])(*start), end="")
        return
    print("(", end="")

    middle = [(s + e) // 2 for s, e in zip(start, end)]
    for state in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        matrixBS([start[i] + (end[i] - middle[i]) * state[i] for i in range(2)],
                 [middle[i] + (end[i] - middle[i]) * state[i] for i in range(2)])
    print(")", end="")


N = int(input())
screen = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
matrixBS((0, 0), (N - 1, N - 1))
