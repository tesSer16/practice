import sys
read = sys.stdin.readline


def force(d, vectors, k):
    if d == N // 2:
        x = y = 0
        for i, v in enumerate(vectors):
            x_val, y_val = dots[v[0]][0] - dots[v[1]][0], dots[v[0]][1] - dots[v[1]][1]
            if k & (1 << i):
                x += x_val
                y += y_val
            else:
                x -= x_val
                y -= y_val

        answer[0] = min((x * x + y * y) ** 0.5, answer[0])
        return

    for i in range(2):
        force(d + 1, vectors, k | i << d)


def dfs(check, vectors):
    if check == MAX1:
        force(0, vectors, 0)
        return

    v1 = -1
    for v in range(N):
        if not check & (1 << v):
            if v1 + 1:
                dfs(check | (1 << v1) | (1 << v), vectors + [(v1, v)])
            else:
                v1 = v


for _ in range(int(read())):
    N = int(input())
    dots = [tuple(map(int, read().split())) for _ in range(N)]
    answer = [float('inf')]
    MAX1 = (1 << N) - 1
    dfs(0, [])
    print(answer[0])
