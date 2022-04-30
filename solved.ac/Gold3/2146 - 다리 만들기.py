import sys
from collections import deque
sys.setrecursionlimit(10**5)


def paint(x, y):
    board[x][y] = color
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N) or not board[nx][ny]:
            continue
        if board[nx][ny] == 1:
            paint(nx, ny)


def bfs(case):
    visit = [b[::] for b in board]
    for r, c, d in Q[case]:
        visit[r][c] = case
    while Q[case]:
        r, c, d = Q[case].popleft()
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if not visit[nr][nc]:
                    Q[case].append((nr, nc, d + 1))
                    visit[nr][nc] = case
                elif visit[nr][nc] != case:
                    return d

    return 10000


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
Q = [deque([(0, 0, 0)]), deque([(0, 0, 0)])]
color = 2
for i in range(N):
    for j in range(N):
        if not board[i][j]:
            continue

        if board[i][j] == 1:
            paint(i, j)
            color += 1
            Q.append(deque())

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if not board[ni][nj] and not visited[ni][nj]:
                    Q[board[i][j]].append((ni, nj, 1))
                    visited[ni][nj] = 1


print(min([bfs(island) for island in range(2, color - 1)]))
