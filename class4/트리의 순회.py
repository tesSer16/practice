import sys
sys.setrecursionlimit(10**6)


def divide(in_i, in_f, post_i, post_f):
    if post_i > post_f or in_i > in_f:
        return
    root = postorder[post_f]
    print(root, end=' ')

    len_right = in_f - pos[root]
    divide(in_i, pos[root] - 1, post_i, post_f - len_right - 1)
    divide(pos[root] + 1, in_f, post_f - len_right, post_f - 1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
pos = {inorder[i]: i for i in range(n)}

divide(0, n - 1, 0, n - 1)
