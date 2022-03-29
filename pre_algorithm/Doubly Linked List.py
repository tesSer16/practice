class Node:
    def __init__(self, el, front=None, back=None):
        self.el = el
        self.front = front
        self.back = back

    def __repr__(self):
        return "(" + repr(self.el) + ")"


class LinkedList:
    def __init__(self, arr=None):
        self._len = len(arr) if arr else 0
        self._head = Node(None)
        self._tail = Node(None, front=self._head)
        self._head.back = self._tail

        if arr:
            for a in arr:
                self.append(a)

    def is_empty(self):
        return self._head.back is self._tail

    def first(self):
        return self._head.back

    def last(self):
        return self._tail.front

    def insert_after(self, n, el):
        p = Node(el, n, n.back)
        n.back.front = p
        n.back = p
        self._len += 1

    def prepend(self, el):
        self.insert_after(self._head, el)

    def append(self, el):
        self.insert_after(self._tail.front, el)

    def __len__(self):
        return self._len

    def __repr__(self):
        return "[" + ', '.join(map(repr, iter(self))) + "]"

    def __iter__(self):
        node = self._head.back
        while node is not self._tail:
            yield node.el
            node = node.back


if __name__ == "__main__":
    l1 = LinkedList()
    print(l1)
