import sys
sys.setrecursionlimit(10**5)


def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > board[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        if not dp[i][j]:
            result = max(result, dfs(i, j))
            print(*dp, sep='\n')
            print()

print(result)
