N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dp[0][1] = [1, 0, 0]

data1 = [(0, 1), (1, 0), (1, 1)]
for x in range(N):
    for y in range(N):
        data2 = [dp[x][y][1], dp[x][y][0], 0]
        data3 = sum(dp[x][y])
        for idx in range(3):
            xi, yi = data1[idx]
            if 0 <= x + xi < N and 0 <= y + yi < N and not sum(board[x + dx][y + dy] for dx in range(xi + 1) for dy in range(yi + 1)):
                dp[x + xi][y + yi][idx] += data3 - data2[idx]

print(sum(dp[N - 1][N - 1]))
