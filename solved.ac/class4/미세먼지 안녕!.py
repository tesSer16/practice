import copy

R, C, T = map(int, input().split())
board = []
cleaner = []
for i in range(R):
    temp = list(map(int, input().split()))
    for j in range(C):
        if temp[j] == -1:
            cleaner.append((i, j))
            temp[j] = 0
    board.append(temp)

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

for _ in range(T):
    next_board = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y]:
                main_dust = board[x][y]
                sub_dust = main_dust // 5
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C and sub_dust and (nx, ny) not in cleaner:
                        next_board[nx][ny] += sub_dust
                        main_dust -= sub_dust
                next_board[x][y] += main_dust

    upper = (lambda r, c:
             1 * (r == cleaner[0][0] and 0 <= c < C - 1) +
             2 * (0 < r <= cleaner[0][0] and c == C - 1) +
             3 * (r == 0 and 0 < c <= C - 1) +
             4 * (0 <= r < cleaner[0][0] and c == 0))

    lower = (lambda r, c:
             1 * (r == cleaner[1][0] and 0 <= c < C - 1) +
             2 * (cleaner[1][0] <= r < R - 1 and c == C - 1) +
             3 * (r == R - 1 and 0 < c <= C - 1) +
             4 * (cleaner[1][0] < r <= R - 1 and c == 0))

    moved_board = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if next_board[x][y]:
                val1, val2 = upper(x, y), lower(x, y)
                dx = dy = 0
                if val1:
                    dx, dy = directions[val1 - 1]
                elif val2:
                    dx, dy = -directions[val2 - 1][0], directions[val2 - 1][1]

                if (x + dx, y + dy) not in cleaner:
                    moved_board[x + dx][y + dy] = next_board[x][y]

    board = copy.deepcopy(moved_board)

print(sum([sum(line) for line in board]))
