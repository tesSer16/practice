import sys
sys.setrecursionlimit(10**6)


def divide(start, end):
    if start > end:
        return

    root = pre_order[start]
    div = end + 1
    for i in range(start + 1, end + 1):
        if root < pre_order[i]:
            div = i
            break

    divide(start + 1, div - 1)
    divide(div, end)
    print(root)


pre_order = list(map(int, sys.stdin.readlines()))
divide(0, len(pre_order) - 1)
