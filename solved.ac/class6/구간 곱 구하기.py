import sys
read = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = (init(start, mid, node * 2) * init(mid + 1, end, node * 2 + 1)) % div
    return tree[node]


def get(start, end, node, left, right):
    if left > end or right < start:
        return 1

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return (get(start, mid, node * 2, left, right) * get(mid + 1, end, node * 2 + 1, left, right)) % div


def update(start, end, node, idx, val):
    if idx < start or idx > end:
        return tree[node]

    if start == end:
        tree[node] = val
        return val

    mid = (start + end) // 2
    tree[node] = (update(start, mid, node * 2, idx, val) * update(mid + 1, end, node * 2 + 1, idx, val)) % div
    return tree[node]


# (M + K) * log(N)
N, M, K = map(int, read().split())
arr = [int(read()) for _ in range(N)]
tree = [1] * (4 * N)
div = 1_000_000_007

init(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, read().split())
    if a == 1:
        update(0, N - 1, 1, b - 1, c)
        arr[b - 1] = c

    if a == 2:
        print(get(0, N - 1, 1, b - 1, c - 1))
