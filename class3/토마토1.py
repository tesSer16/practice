import sys
sys.setrecursionlimit(10**5)


def day(riped):
    def ripe(a, b, c):
        if a < 0 or b < 0 or c < 0 or a >= H or b >= N or c >= M:
            return
        if tomatoes[a][b][c]:
            return

        tomatoes[a][b][c] = 1
        temp.append((a, b, c))

    temp = []
    for _ in range(len(riped)):
        cur_tomato = riped.pop()
        for s in states:
            ripe(*map(lambda x: x[0] + x[1], zip(cur_tomato, s)))

    riped += temp


def last_check():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if not tomatoes[i][j][k]:
                    return True
    return False


M, N, H = map(int, input().split())
tomatoes = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
ripe_tomatoes = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 1:
                ripe_tomatoes.append((i, j, k))

states = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))
cnt = 0
while ripe_tomatoes:
    day(ripe_tomatoes)
    cnt += 1

if last_check():
    print(-1)
else:
    print(cnt - 1)
