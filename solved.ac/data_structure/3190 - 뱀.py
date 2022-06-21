from collections import deque


N, K = int(input()), int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = -1

L = int(input())
data = {}
for _ in range(L):
    a, b = input().split()
    data[int(a)] = b


board[0][0] = 1
direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
idx = 0
snake = deque([(0, 0)])
time = 0

while True:
    if time in data:
        idx = (idx + {'L': -1, 'D': 1}[data[time]]) % 4

    dx, dy = direc[idx]
    nx, ny = snake[0][0] + dx, snake[0][1] + dy
    if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 1:
        break

    snake.appendleft((nx, ny))

    if board[nx][ny] != -1:
        tx, ty = snake.pop()
        board[tx][ty] = 0

    board[nx][ny] = 1
    time += 1

print(time + 1)
