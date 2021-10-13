from collections import deque


def bfs(x, y):
    q = deque([(x, y, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    candidate = []

    while q:
        x, y, d = q.popleft()
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] <= size:
                visited[nx][ny] = 1

                if 0 < board[nx][ny] < size:
                    candidate.append((nx, ny, d + 1))
                if not candidate:
                    q.append((nx, ny, d + 1))

    return min(candidate, key=lambda t: (t[2], t[0], t[1])) if candidate else []


N = int(input())
board = []
pos = ()
for i in range(N):
    temp = list(map(int, input().split()))
    if not pos and 9 in temp:
        pos = (i, temp.index(9))
    board.append(temp)

size, cnt, time = 2, 0, 0
board[pos[0]][pos[1]] = 0
while True:
    data = bfs(*pos)
    if not data:
        print(time)
        break
    i, j = data[0], data[1]
    time += data[2]
    board[i][j] = 0
    cnt += 1
    if cnt == size:
        cnt = 0
        size += 1
    pos = (i, j)
