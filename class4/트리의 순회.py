def divide(_in, _post):
    if not _post:
        return
    root = _post[-1]
    print(root, end=" ")
    if _post[0] == root:
        return

    root_index = _in.index(root)
    left_in = _in[:root_index]
    right_in = _in[root_index + 1:]

    boundary = -len(right_in) - 1
    left_post = _post[:boundary]
    right_post = _post[boundary:-1]

    divide(left_in, left_post)
    divide(right_in, right_post)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

divide(inorder, postorder)
