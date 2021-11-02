import sys

for _ in range(int(input())):
    n, m = map(int, sys.stdin.readline().split())
    commands = list(sys.stdin.readline().strip())
    x1, y1, x2, y2 = 0, 0, n - 1, m - 1
    move = {'R': (0, 1), 'D': (1, 0), 'U': (-1, 0), 'L': (0, -1)}
    tot_dx = tot_dy = 0
    for command in commands:
        dx, dy = move[command]
        nx1, nx2 = x1 + dx, x2 + dx
        ny1, ny2 = y1 + dy, y2 + dy

        if nx2 < 0 or nx1 > n - 1 or ny2 < 0 or ny1 > m - 1:
            break
        else:
            tot_dx += dx
            tot_dy += dy
            x1 = min(n - 1, max(0, nx1))
            x2 = min(n - 1, max(0, nx2))
            y1 = min(m - 1, max(0, ny1))
            y2 = min(m - 1, max(0, ny2))

    print(x1 + 1 - tot_dx, y1 + 1 - tot_dy)
