def dfs(mode, depth=0, lx=-1, ly=-1, s=""):
    print(lx, ly)
    if depth == N + 1:
        print(s)
        if s and (int(s) ** 0.5).is_integer():
            ans[mode] = max(ans[mode], int(s))
        return

    for x in range(lx, lx + 2):
        if x == -1 or x == N:
            continue

        for y in range(ly, M + 1):
            if y == -1 or (x == lx and y == ly):
                continue

            if y == M:
                dfs(mode, depth + 1, lx, ly, s)
            else:
                dfs(mode, depth + 1, x, y, s + board[x][y])


N, M = map(int, input().split())
board = [input() for _ in range(N)]

ans = [0, 0]
dfs(0)

for r in range(N):
    board[r] = board[r][::-1]

print("------")
dfs(1)

print(max(ans))
