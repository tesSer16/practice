from collections import deque
import sys


def bfs():
    q = deque([(0, 0, 1)])
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1
    while q:
        x, y, level = q.popleft()
        if (x, y) == (N - 1, M - 1):
            return visited[x][y][level]
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not board[nx][ny] and not visited[nx][ny][level]:
                    q.append((nx, ny, level))
                    visited[nx][ny][level] = visited[x][y][level] + 1
                elif board[nx][ny] and level:
                    visited[nx][ny][0] = visited[x][y][level] + 1
                    q.append((nx, ny, 0))

    return -1


N, M = map(int, input().split())
board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

print(bfs())
