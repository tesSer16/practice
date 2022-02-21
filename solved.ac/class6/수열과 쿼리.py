import sys
read = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node][0] = arr[start]
        tree[node][1] = start
        return tree[node]

    mid = (start + end) // 2
    s = init(start, mid, 2 * node)
    e = init(mid + 1, end, 2 * node + 1)
    if s[0] < e[0]:
        tree[node][0] = s[0]
        tree[node][1] = s[1]
    elif s[0] == e[0]:
        tree[node][0] = s[0]
        tree[node][1] = min(s[1], e[1])
    else:
        tree[node][0] = e[0]
        tree[node][1] = e[1]

    return tree[node]


def update(start, end, node, idx, value):
    if not (start <= idx <= end):
        return tree[node]

    if start == end:
        arr[idx] = value
        tree[node][0] = value
        return tree[node]

    mid = (start + end) // 2
    s = update(start, mid, 2 * node, idx, value)
    e = update(mid + 1, end, 2 * node + 1, idx, value)
    if s[0] < e[0]:
        tree[node][0] = s[0]
        tree[node][1] = s[1]
    elif s[0] == e[0]:
        tree[node][0] = s[0]
        tree[node][1] = min(s[1], e[1])
    else:
        tree[node][0] = e[0]
        tree[node][1] = e[1]

    return tree[node]


def find(start, end, node, left, right):
    if right < start or end < left:
        return

    if left <= start and end <= right:
        if _min[0] > tree[node][0]:
            _min[0] = tree[node][0]
            _min[1] = tree[node][1]

        return

    mid = (start + end) // 2
    find(start, mid, 2 * node, left, right)
    find(mid + 1, end, 2 * node + 1, left, right)


N = int(read())
arr = list(map(int, read().split()))

tree = [[10**9 + 1, -1] for _ in range(4 * N)]
init(0, N - 1, 1)
for _ in range(int(read())):
    a, b, c = map(int, read().split())
    if a == 1:
        update(0, N - 1, 1, b - 1, c)
    else:
        _min = [10 ** 9 + 1, -1]
        find(0, N - 1, 1, b - 1, c - 1)
        print(_min[1] + 1)
