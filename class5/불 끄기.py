def dfs(depth, board, k):
    new = board[::]
    if depth == N:
        check(new, sum(map(int, format(k, 'b'))))
        return

    dfs(depth + 1, new, k)
    click(0, depth, new)
    dfs(depth + 1, new, k | 1 << depth)


def check(case, base):
    global answer
    cnt = base
    for x in range(1, N):
        for y in range(N):
            if case[x - 1] & (1 << y):
                click(x, y, case)
                cnt += 1

    if not case[N - 1]:
        answer = min(answer, cnt)


def click(x, y, _board):
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1), (0, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            _board[nx] ^= 1 << ny


N = 10
origin = [0] * N
for i in range(N):
    data = input()
    for j in range(N):
        if data[j] == "O":
            origin[i] += 1 << j
answer = 100

dfs(0, origin, 0)
print(answer)
