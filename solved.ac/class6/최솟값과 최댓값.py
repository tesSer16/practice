import sys
read = sys.stdin.readline


def init(start, end, node):
    if start == end:
        seg_tree[node][0] = arr[start]
        seg_tree[node][1] = arr[start]
        return seg_tree[node]

    mid = (start + end) // 2
    s = init(start, mid, 2 * node)
    e = init(mid + 1, end, 2 * node + 1)
    seg_tree[node][0] = min(s[0], e[0])
    seg_tree[node][1] = max(s[1], e[1])

    return seg_tree[node]


def find(start, end, left, right, node):
    global _min, _max
    if left > end or right < start:
        return

    if left <= start and end <= right:
        _min = min(_min, seg_tree[node][0])
        _max = max(_max, seg_tree[node][1])
        return

    mid = (start + end) // 2
    find(start, mid, left, right, 2 * node)
    find(mid + 1, end, left, right, 2 * node + 1)


N, M = map(int, read().split())
seg_tree = [[10 ** 9, 1] for _ in range(4 * N)]
arr = [int(read()) for _ in range(N)]
init(0, N - 1, 1)

for _ in range(M):
    a, b = map(int, read().split())
    _min, _max = 10 ** 9, 1
    find(0, N - 1, a - 1, b - 1, 1)
    print(_min, _max)
