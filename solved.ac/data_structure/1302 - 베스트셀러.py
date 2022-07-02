import sys
read = sys.stdin.readline


cards = {}
for _ in range(int(read())):
    n = read().strip()
    cards[n] = cards.get(n, 0) + 1

_max = (None, -1)
for k, v in sorted(cards.items()):
    if _max[1] < v:
        _max = (k, v)

print(_max[0])
