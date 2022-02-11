import sys
input = sys.stdin.readline


def chain(a, b):
    if a < 0 or a >= N or b < 0 or b >= M:
        return
    if not ground[a][b]:
        return

    ground[a][b] = 0

    chain(a - 1, b)
    chain(a + 1, b)
    chain(a, b + 1)
    chain(a, b - 1)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j]:
                chain(i, j)
                answer += 1

    print(answer)
