def dfs(x, y, depth, _sum):
    if depth == 3:
        data[0] = max(_sum, data[0])
        return
    if data[0] >= _sum + (3 - depth) * data[1]:
        return

    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny]:
            continue

        visited[nx][ny] = 1
        if depth == 1:
            dfs(x, y, depth + 1, _sum + board[nx][ny])
        dfs(nx, ny, depth + 1, _sum + board[nx][ny])
        visited[nx][ny] = 0


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
data = [0, max(map(max, board))]

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, board[i][j])
        visited[i][j] = 0

print(data[0])
