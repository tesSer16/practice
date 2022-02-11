import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**4)


def check():
    for x in range(h):
        for y in range(w):
            if is_first and 0 < x < h - 1 and 0 < y < w - 1:
                continue

            if not visited[x] & (1 << y) and board[x][y] != '*' and old[x] & (1 << y):
                visited[x] |= 1 << y
                search(x, y)


def search(x, y):
    global ans
    s = str(board[x][y])
    if s == '*':
        return

    if ord('A') <= ord(s) <= ord('Z'):
        if s.lower() not in key:
            return
        change(x, y)
    if ord('a') <= ord(s) <= ord('z'):
        change(x, y)
        key.add(s)
    if s == '$':
        change(x, y)
        ans += 1

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and not visited[nx] & (1 << ny):
            visited[nx] |= 1 << ny
            search(nx, ny)


def change(x, y):
    global is_changed
    board[x][y] = '.'
    is_changed = True


for _ in range(int(read())):
    h, w = map(int, read().split())

    board = []
    for _ in range(h):
        board.append(list(read().strip()))

    key = set()
    temp = read().strip()
    if temp != '0':
        for t in temp:
            key.add(t)

    ans = 0
    is_changed = True
    is_first = True
    old = [(1 << w) - 1] * h
    while is_changed:
        visited = [0] * h
        is_changed = False
        check()
        is_first = False
        old = visited[::]

        # print(*board, sep='\n')
        # print()

    print(ans)
