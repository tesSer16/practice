def dfs(depth):
    if depth == max_depth:
        for line in board:
            print(''.join(map(str, line)))
        exit(0)

    x, y = candidates[depth]
    nx, ny = x // 3, y // 3
    for n in range(1, 10):
        if not row_check[x][n] and not column_check[y][n] and not block_check[nx][ny][n]:
            board[x][y] = n
            row_check[x][n] = 1
            column_check[y][n] = 1
            block_check[nx][ny][n] = 1

            dfs(depth + 1)
            row_check[x][n] = 0
            column_check[y][n] = 0
            block_check[nx][ny][n] = 0


board = []
row_check = [[0] * 10 for _ in range(9)]
column_check = [[0] * 10 for _ in range(9)]
block_check = [[[0] * 10 for _ in range(3)] for _ in range(3)]
candidates = []

for i in range(9):
    row = list(map(int, input()))
    for j, num in enumerate(row):
        if not num:
            candidates.append((i, j))
        else:
            row_check[i][num] = 1
            column_check[j][num] = 1
            block_check[i // 3][j // 3][num] = 1
    board.append(row)

max_depth = len(candidates)

dfs(0)
