import sys
read = sys.stdin.readline


def find(x, weight):
    if x != b[x]:
        return find(b[x], weight + ip[x])
    return weight


for _ in range(int(read())):
    n = int(read())
    b = [0] + list(map(int, read().split()))
    p = [0] + list(map(int, read().split()))
    ip = {k: v for v, k in enumerate(p)}
    data = sorted([(find(u, 0), u) for u in range(1, n + 1)])
    print(data)
