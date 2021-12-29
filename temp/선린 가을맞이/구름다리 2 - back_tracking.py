import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
color = [''] + [0] * N
connected = [[] for _ in range(N + 1)]

for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())
    connected[v].append(w)
    connected[w].append(v)


def check(v1, clr):
    for v2 in connected[v1]:
        if color[v2] == clr:
            return False

    return True


def dfs(depth):
    if depth == N + 1:
        print(*(color[1:]), sep=' ')
        exit()

    for c in range(1, N + 1):
        if check(depth, c):
            color[depth] = c
            dfs(depth + 1)


dfs(1)
