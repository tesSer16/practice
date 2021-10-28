N = int(input())

blank = [[], []]
board = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            if (i + j) % 2 == 0:
                blank[0].append((i, j))
            else:
                blank[1].append((i, j))
    board.append(line)


M = [len(blank[0]), len(blank[1])]
result = [0, 0]


def dfs(depth, cnt, rest, idx):
    if depth == M[idx] or rest == 0:
        result[idx] = max(cnt, result[idx])
        return
    if rest + cnt <= result[idx]:
        return

    x, y = blank[idx][depth]
    if board[x][y]:
        board[x][y] = 0
        dfs(depth + 1, cnt, rest - 1, idx)
        temp = []
        count = 0
        for dx, dy in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
            for k in range(1, N):
                nx, ny = x + k * dx, y + k * dy
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny]:
                        board[nx][ny] = 0
                        count += 1
                        temp.append((nx, ny))
                else:
                    break

        dfs(depth + 1, cnt + 1, rest - count - 1, idx)

        for rx, ry in temp:
            board[rx][ry] = 1

        board[x][y] = 1

    else:
        dfs(depth + 1, cnt, rest, idx)


dfs(0, 0, M[0], 0)
dfs(0, 0, M[1], 1)
print(sum(result))
