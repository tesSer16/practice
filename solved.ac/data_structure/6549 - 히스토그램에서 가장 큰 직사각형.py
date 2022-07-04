import sys
read = sys.stdin.readline


def init(left, right, node):
    if left == right:
        seg_tree[node] = (arr[left], arr[left])
        return seg_tree[node]

    mid = left + (right - left) // 2
    l, r = init(left, mid, 2 * node), init(mid + 1, right, 2 * node + 1)
    seg_tree[node] = (min(l[0], r[0]), max(l[1], r[1]))

    return seg_tree[node]


def check(left, right, node, idx):
    # print(left, right, idx, seg_tree[node])
    global cnt
    cnt += 1
    if left == right:
        if arr[idx] > arr[left]:
            return -1, -1
        return left, right

    if left > idx:
        return -1, -1

    mid = (left + right) // 2

    a = b = -1
    if arr[idx] <= seg_tree[node][0]:
        a, b = left, right
    elif arr[idx] > seg_tree[node][1]:
        pass
    else:  # seg_tree[node][0] <= arr[idx] <= seg_tree[node][1]
        left_range = check(left, mid, 2 * node, idx)
        right_range = check(mid + 1, right, 2 * node + 1, idx)
        a, b = left_range[0], right_range[1]
        if a == -1 and b == -1:
            pass
        elif a == -1:
            a, b = right_range
        elif b == -1:
            a, b = left_range
        elif left_range[1] + 1 != right_range[0]:
            if left_range[0] <= idx <= left_range[1]:
                a, b = left_range
            elif right_range[0] <= idx <= right_range[1]:
                a, b = right_range
            else:
                a = b = -1

    # print(left, right, a, b)
    return a, b


MAX = float('inf')
while True:
    # temp = read()
    # if temp[0] == "0":
    #     break

    cnt = 0
    # N, *arr = map(int, temp.split())
    N = 100000
    arr = [1, 1, 2, 2] * (N // 4)

    seg_tree = [(MAX, 0) for _ in range(4 * N)]
    init(0, N - 1, 1)
    _max = 0
    for i in range(N):
        if i and arr[i - 1] == arr[i]:
            pass
        elif arr[i] and arr[i] * N > _max:
            A, B = check(0, N - 1, 1, i)
            if A == -1 or not A <= i <= B:
                A = B = i
            _max = max(_max, arr[i] * (B - A + 1))
            # print(A, B, i)
    print(_max, cnt)
    break
