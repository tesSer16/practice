def dfs(x, y, dx, dy, s):
    s1, s2 = int(s), int(s[::-1])
    for t in (s1, s2):
        if (t**0.5).is_integer() and t > ans[0]:
            ans[0] = t

    nx, ny = x + dx, y + dy
    if not (0 <= nx < N and 0 <= ny < M):
        return

    dfs(nx, ny, dx, dy, s + board[nx][ny])


N, M = map(int, input().split())
board = [input() for _ in range(N)]
ans = [-1]
for i in range(N):
    for j in range(M):
        for di in range(-N, N + 1):
            for dj in range(-M, M + 1):
                if di == 0 and dj == 0:
                    continue
                dfs(i, j, di, dj, board[i][j])

print(ans[0])
