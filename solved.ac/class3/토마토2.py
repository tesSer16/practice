import sys


def day(riped):
    def ripe(a, b):
        if 0 <= a < N and 0 <= b < M and not tomatoes[a][b]:
            tomatoes[a][b] = 1
            temp.append((a, b))
        else:
            return

    temp = []
    for _ in range(len(riped)):
        cur_tomato = riped.pop()
        for s in states:
            ripe(*map(lambda x: x[0] + x[1], zip(cur_tomato, s)))

    riped += temp


def last_check():
    for i in range(N):
        for j in range(M):
            if not tomatoes[i][j]:
                return True
    return False


M, N = map(int, input().split())
tomatoes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ripe_tomatoes = []
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            ripe_tomatoes.append((i, j))

states = ((1, 0), (0, 1), (-1, 0), (0, -1))
cnt = 0
while ripe_tomatoes:
    day(ripe_tomatoes)
    cnt += 1

if last_check():
    print(-1)
else:
    print(cnt - 1)
