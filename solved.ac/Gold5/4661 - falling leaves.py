class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if key > root.data:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)

    return root


def travel(root):
    if root is None:
        return
    print(root.data, end="")
    travel(root.left)
    travel(root.right)


finished = False
while not finished:
    data = []
    while True:
        datum = input().strip()
        if datum == '*':
            break
        if datum == '$':
            finished = True
            break
        data.append(datum)

    ans = Node(data[-1])
    for i in range(len(data) - 2, -1, -1):
        for c in data[i]:
            insert(ans, c)

    travel(ans)
    print()
