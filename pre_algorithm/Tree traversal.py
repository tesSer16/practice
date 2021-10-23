# mid left right
def preorder_traversal(tree, start):
    def travel(v):
        print(v if v != '.' else '', end="")
        for c in tree.get(v, []):
            travel(c)

    travel(start)
    print()


# left mid right
def inorder_traversal(tree, start):
    def travel(v):
        for i, c in enumerate(tree.get(v, [])):
            if i == 1 and v != '.':
                print(v, end="")
            travel(c)
        if len(tree.get(v, [])) <= 1 and v != '.':
            print(v, end="")

    travel(start)
    print()


# left right mid
def postorder_traversal(tree, start):
    def travel(v):
        for c in tree.get(v, []):
            travel(c)

        print(v if v != '.' else '', end="")
    travel(start)
    print()


if __name__ == "__main__":
    N = int(input())
    dict_tree = {}
    for _ in range(N):
        node, left, right = input().split()
        dict_tree[node] = []
        for child in (left, right):
            dict_tree[node].append(child)

    preorder_traversal(dict_tree, 'A')
    inorder_traversal(dict_tree, 'A')
    postorder_traversal(dict_tree, 'A')
