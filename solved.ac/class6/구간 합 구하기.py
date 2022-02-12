import sys
read = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]


def get_sum(start, end, node, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return get_sum(start, mid, node * 2, left, right) + get_sum(mid + 1, end, node * 2 + 1, left, right)


def update(start, end, node, idx, diff):
    if idx < start or idx > end:
        return

    tree[node] += diff
    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, idx, diff)
    update(mid + 1, end, node * 2 + 1, idx, diff)


# (M + K) * log(N)
N, M, K = map(int, read().split())
arr = [int(read()) for _ in range(N)]
tree = [0] * (4 * N)
init(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, read().split())
    if a == 1:
        update(0, N - 1, 1, b - 1, c - arr[b - 1])
        arr[b - 1] = c
    if a == 2:
        print(get_sum(0, N - 1, 1, b - 1, c - 1))
