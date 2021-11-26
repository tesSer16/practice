import sys
read = sys.stdin.readline


def dfs(v, friend):
    if answer[0]:
        return
    if len(data[v]) == 1:
        answer[0] = 1
        return


for _ in range(int(read())):
    n, k = map(int, read().split())
    x = list(map(int, read().split()))
    data = [[] for _ in range(n + 1)]
    answer = [0]
    for _ in range(n - 1):
        v1, v2 = map(int, read().split())
        data[v1].append(v2)
        data[v2].append(v1)