import copy
from itertools import combinations


def spread(r, c):
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and not board[nr][nc]:
            board[nr][nc] = 2
            spread(nr, nc)


N, M = map(int, input().split())
origin = []
virus = []
zeros = []

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j] == 0:
            zeros.append((i, j))
        elif temp[j] == 2:
            virus.append((i, j))
    origin.append(temp)

safe = 0
for case in combinations(zeros, 3):
    board = copy.deepcopy(origin)
    for a, b in list(case):
        board[a][b] = 1

    for x, y in virus:
        spread(x, y)

    safe = max(sum([line.count(0) for line in board]), safe)

print(safe)
