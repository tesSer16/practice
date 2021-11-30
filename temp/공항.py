import bisect


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


N, M, K = map(int, input().split())
parent = list(range(M))
card_pool = sorted(list(map(int, input().split())))

for b in list(map(int, input().split())):
    v = bisect.bisect_right(card_pool, b)
    w = find(v)
    print(card_pool[w])

    if w < M - 1:
        parent[find(w)] = find(w + 1)
