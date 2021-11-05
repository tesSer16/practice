def dfs(x, y, d):
    result[0] = max(result[0], d)
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visited[ord(board[nx][ny]) - 65]:
            visited[ord(board[nx][ny]) - 65] = 1
            dfs(nx, ny, d + 1)
            visited[ord(board[nx][ny]) - 65] = 0


R, C = map(int, input().split())
board = [input() for _ in range(R)]
visited = [0] * 26
visited[ord(board[0][0]) - 65] = 1
result = [0]
dfs(0, 0, 1)
print(result[0])
