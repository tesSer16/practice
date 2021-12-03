import sys
read = lambda: int(sys.stdin.readline())


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


G, P = read(), read()
parent = list(range(G + 1))

c = 0
for c in range(P):
    w = find(read())
    if not w:
        break
    parent[w] = parent[w - 1]

print(c)
