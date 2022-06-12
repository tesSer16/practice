class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def make_tree(root_label):
    root = Node(root_label)
    lc, rc = dict_tree[root.data]
    root.left = make_tree(lc) if lc != '.' else None
    root.right = make_tree(rc) if rc != '.' else None

    return root


def preorder(t):
    if t:
        print(t.data, end="")
        preorder(t.left)
        preorder(t.right)


def inorder(t):
    if t:
        inorder(t.left)
        print(t.data, end="")
        inorder(t.right)


def postorder(t):
    if t:
        postorder(t.left)
        postorder(t.right)
        print(t.data, end="")


if __name__ == "__main__":
    N = int(input())
    dict_tree = {}
    for _ in range(N):
        parent, left, right = input().split()
        dict_tree[parent] = [left, right]

    tree = make_tree('A')
    preorder(tree)
    print()
    inorder(tree)
    print()
    postorder(tree)
    print()
