def move(d, board):
    new_board = [[0] * N for _ in range(N)]
    data = [(1, 0, 0, 1, 1, 0, 0), (-1, 1, 0, 0, 0, 1, 0),
            (-1, 0, 1, 0, 1, 0, 0), (1, 1, 0, 0, 0, 0, 1)][d]

    for a in range(N):
        stack = []
        for b in range(N)[::data[0]]:
            r = a * data[1] + b * (data[1] ^ 1)
            c = b * data[1] + a * (data[1] ^ 1)
            if not board[r][c]:
                continue
            if stack and stack[-1] == [board[r][c]]:
                stack[-1].append(board[r][c])
            else:
                stack.append([board[r][c]])

            for k in range(len(stack)):
                x = r * data[1] + (N - 1 - k) * data[2] + k * data[3]
                y = c * data[4] + (N - 1 - k) * data[5] + k * data[6]
                new_board[x][y] = sum(stack[k])

    return new_board


def dfs(d, current):
    if d == 5:
        mb = max(max(c) for c in current)
        result[0] = max(result[0], mb)
        return

    for i in range(4):
        dfs(d + 1, move(i, current))


N = int(input())
origin = [list(map(int, input().split())) for _ in range(N)]
result = [0]
dfs(0, origin)
print(result[0])
