import sys
read = sys.stdin.readline


class Node:
    def __init__(self):
        self.data = {}
        self.leaf = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, _list):
        current = self.root
        for num in _list:
            if current.leaf:
                return False
            if num not in current.data:
                current.data[num] = Node()

            current = current.data[num]

        current.leaf = True
        return True

    def search(self, _list):
        current = self.root
        for num in _list:
            if current.leaf:
                return False

            current = current.data[num]
        return True


for _ in range(int(read())):
    N = int(read())
    trie = Trie()
    phone_list = [read().strip() for _ in range(N)]

    for p in phone_list:
        trie.insert(p)

    for p in phone_list:
        if not trie.search(p):
            print("NO")
            break
    else:
        print("YES")
