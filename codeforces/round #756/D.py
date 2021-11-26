import sys
read = sys.stdin.readline


for _ in range(int(read())):
    n = int(read())
    b = [0] + list(map(int, read().split()))
    p = [0] + list(map(int, read().split()))
    dist = [0] * (n + 1)
    w = [-1] * (n + 1)
    for i in range(1, n + 1):
        dist[p[i]] = i - 1

    w[p[1]] = 0
    answer = 0
    for i in range(2, n + 1):
        if w[b[p[i]]] == -1:
            answer = -1
            break
        w[p[i]] = dist[p[i]] - dist[b[p[i]]]

    if answer:
        print(-1)
    else:
        print(*w[1:])
