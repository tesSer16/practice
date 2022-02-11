import sys
from collections import deque


def day():
    def ripe(a, b, c):
        if a < 0 or b < 0 or c < 0 or a >= H or b >= N or c >= M:
            return
        if tomatoes[a][b][c]:
            return

        tomatoes[a][b][c] = 1
        ripe_tomatoes.append((a, b, c))

    for _ in range(len(ripe_tomatoes)):
        cur_tomato = ripe_tomatoes.popleft()
        for s in states:
            ripe(*map(sum, zip(cur_tomato, s)))


def last_check():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if not tomatoes[i][j][k]:
                    return True
    return False


M, N, H = map(int, input().split())
ripe_tomatoes = deque()
tomatoes = []
for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(M):
            if temp[j][k] == 1:
                ripe_tomatoes.append((i, j, k))
    tomatoes.append(temp)

states = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))
cnt = 0
while ripe_tomatoes:
    day()
    cnt += 1

if last_check():
    print(-1)
else:
    print(cnt - 1)
