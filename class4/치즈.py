import copy


def check(x, y):
    contacted = 0
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not board[nx][ny]:
            contacted += 1

    return contacted


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
cheese = copy.deepcopy(board)
q = []
for i in range(N):
    for j in range(M):
        if board[i][j]:
            temp = check(i, j)
            cheese[i][j] = temp
            if temp >= 2:
                q.append((i, j))

print(*cheese, sep='\n')
hour = 0
temp = []
while q:
    x, y = q.pop()
    board[x][y] = cheese[x][y] = 0
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny]:
            cheese[nx][ny] += 1
            if cheese[nx][ny] >= 2:
                temp.append((nx, ny))

print(hour)
