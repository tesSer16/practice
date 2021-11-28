import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find(s, d):
    if check[s] >= 0:
        k = 0
        visited = i
        while k < d and visited != s:
            check[visited] = 1
            k += 1
            visited = data[visited]
        while k < d:
            check[visited] = 0
            k += 1
            visited = data[visited]
        return

    check[s] = 0
    find(data[s], d + 1)


for _ in range(int(read())):
    n = int(read())
    data = [0] + list(map(int, read().split()))
    check = [-1] * (n + 1)
    for i in range(1, n + 1):
        find(i, 0)
    print(sum(check) + 1)
