import copy
import sys
sys.setrecursionlimit(10**5)


def check(r, c):
    contacted = 0
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if not board[nr][nc] and visited[nr][nc] == -1:
            contacted += 1

    return contacted


def void(r, c, value):
    visited[r][c] = value
    void_temp.append((r, c))
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and not board[nr][nc] and not visited[nr][nc]:
            void(nr, nc, value)


def delete_void(value):
    for v in void_list[-value - 1]:
        r, c = v
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if board[nr][nc]:
                cheese[nr][nc] += 1
                if cheese[nr][nc] >= 2 and (nr, nc) not in q:
                    temp.add((nr, nc))

        visited[r][c] = -1


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
cheese = copy.deepcopy(board)
visited = [[0] * M for _ in range(N)]
val = -1
void_list = []
for i in range(N):
    for j in range(M):
        if not board[i][j] and not visited[i][j]:
            void_temp = []
            void(i, j, val)
            void_list.append(void_temp)
            val -= 1


q = set()
for i in range(N):
    for j in range(M):
        if board[i][j]:
            temp = check(i, j)
            cheese[i][j] = temp
            if temp >= 2:
                q.add((i, j))

hour = 0
while q:
    # print(*cheese, sep='\n')
    # print(q)
    # print()
    temp = set()
    for x, y in q:
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if board[nx][ny] and (nx, ny) not in q:
                cheese[nx][ny] += 1
                if cheese[nx][ny] >= 2:
                    temp.add((nx, ny))
            elif visited[nx][ny] < -1:
                delete_void(visited[nx][ny])

        board[x][y] = cheese[x][y] = 0

    q = temp
    hour += 1

print(hour)
