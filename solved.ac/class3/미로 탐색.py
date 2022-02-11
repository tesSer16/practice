import sys
from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
maze[0][0] = 1


def bfs():
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    q = deque([(0, 0, 1)])
    visited = []

    while q:
        node = q.popleft()
        for d in directions:
            x, y = node[0] + d[0], node[1] + d[1]
            if 0 <= x < N and 0 <= y < M and maze[x][y] == 1 and (x, y) not in visited:
                maze[x][y] = maze[node[0]][node[1]] + 1
                q.append((x, y, node[2] + 1))
                visited.append((x, y))

            if (x, y) == (N - 1, M - 1):
                return q[-1][2]


print(bfs())
