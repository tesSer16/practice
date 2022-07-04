import sys
sys.setrecursionlimit(10**8)
read = sys.stdin.readline


def merge(left, right):
    return left if left[0] < right[0] else right


def init(start, end, node):
    if start == end:
        seg_tree[node] = [arr[start], start]
        return seg_tree[node]

    mid = start + (end - start) // 2
    l, r = init(start, mid, 2 * node), init(mid + 1, end, 2 * node + 1)
    seg_tree[node] = merge(l, r)

    return seg_tree[node]


def search(start, end, left, right, node):
    if start > right or end < left:
        return [MAX, -1]

    if left <= start and end <= right:
        return seg_tree[node]

    mid = start + (end - start) // 2
    l = search(start, mid, left, right, 2 * node)
    r = search(mid + 1, end, left, right, 2 * node + 1)

    return merge(l, r)


def solve(start, end):
    global cnt
    cnt += 1
    if start > end:
        return -1
    if start == end:
        return arr[end]

    _min, idx = search(0, N - 1, start, end, 1)

    l = solve(start, idx - 1)
    r = solve(idx + 1, end)
    c = _min * (end - start + 1)

    return max(l, r, c)


cnt = 0
MAX = float('inf')
while True:
    # arr = list(map(int, read().split()))
    M = 10
    arr = [M] + [*range(1, M + 1)]
    if arr[0] == 0:
        break
    N = arr.pop(0)
    seg_tree = [[0, 0] for _ in range(4 * N)]

    init(0, N - 1, 1)
    print(solve(0, N - 1), cnt)
    break
