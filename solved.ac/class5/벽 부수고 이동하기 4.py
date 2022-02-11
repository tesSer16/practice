import sys
sys.setrecursionlimit(10**6)


def check(x, y):
    result = 0
    added = []
    for dx, dy in direc:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and block[nx][ny][0] and block[nx][ny][1] not in added:
            result += block[nx][ny][0]
            added.append(block[nx][ny][1])

    return result


def search(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1
    _list.append((x, y))

    for dx, dy in direc:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            search(nx, ny)


N, M = map(int, input().split())
direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
block = [[[0, 0] for _ in range(M)] for _ in range(N)]
_map = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j, s in enumerate(input()):
        _map[i][j] = int(s)
        visited[i][j] = int(s)

idx = 0
for i in range(N):
    for j in range(M):
        if not _map[i][j] and block[i][j][0] == 0:
            cnt = 0
            _list = []
            search(i, j)

            for r, c in _list:
                block[r][c][0] = cnt
                block[r][c][1] = idx
            idx += 1

            # print(*block, sep='\n')

for i in range(N):
    for j in range(M):
        if _map[i][j]:
            print((check(i, j) + 1) % 10, end="")
        else:
            print(0, end="")
    print()
