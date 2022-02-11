def move(xr, yr, xb, yb, d):
    dx, dy = direc[d]
    rcnt = bcnt = 0
    while True:
        nxb, nyb = xb + dx, yb + dy
        if board[nxb][nyb] == 'O':
            return False
        if board[nxb][nyb] == '#':
            break
        xb, yb = nxb, nyb
        bcnt += 1

    while True:
        nxr, nyr = xr + dx, yr + dy
        if board[nxr][nyr] == 'O':
            return -1
        if board[nxr][nyr] == '#':
            break
        xr, yr = nxr, nyr
        rcnt += 1

    if (xb, yb) == (xr, yr):
        if bcnt < rcnt:
            xr -= dx
            yr -= dy
        else:
            xb -= dx
            yb -= dy

    return (xr, yr), (xb, yb)


def bfs():
    check = {(R, B)}
    q = [(R, B)]
    n = 1
    while q and n < 11:
        nq = []
        for r, b in q:
            for d in range(4):
                data = move(*r, *b, d)
                if data == -1:
                    return n
                if data and data not in check:
                    check.add(data)
                    nq.append(data)
        n += 1
        q = nq[::]

    return -1


N, M = map(int, input().split())
board = []
R = B = None
for i in range(N):
    temp = input()
    for j in range(M):
        if temp[j] == 'B':
            B = (i, j)
        if temp[j] == 'R':
            R = (i, j)
    board.append(temp)

direc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
print(bfs())
