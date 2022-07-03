import sys
read = sys.stdin.readline


class Node:
    def __init__(self):
        self.min = float('inf')
        self.max = -float('inf')
        self.left = None
        self.right = None


def init(left, right, tree):
    if left == right:
        val = arr[left]
        tree.min = tree.max = val
        return val, val

    tree.left, tree.right = Node(), Node()
    mid = (left + right) // 2
    l_min, l_max = init(left, mid, tree.left)
    r_min, r_max = init(mid + 1, right, tree.right)
    tree.min = min(l_min, r_min)
    tree.max = max(l_max, r_max)

    return tree.min, tree.max


def search(left, right, a, b, tree):
    if left > b or right < a:
        return float('inf'), -float('inf')

    if a <= left and right <= b:
        return tree.min, tree.max

    mid = (left + right) // 2
    l_min, l_max = search(left, mid, a, b, tree.left)
    r_min, r_max = search(mid + 1, right, a, b, tree.right)
    return min(l_min, r_min), max(l_max, r_max)


N, M = map(int, read().split())
arr = [int(read()) for _ in range(N)]
root = Node()
init(0, N - 1, root)
for _ in range(M):
    A, B = map(int, read().split())
    print(*search(0, N - 1, A - 1, B - 1, root))
