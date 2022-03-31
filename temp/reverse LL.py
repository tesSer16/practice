class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


# data is list
class LinkedList:
    def __init__(self, data):
        self.head = Node(None)

        node = self.head

        for d in data:
            node.next = Node(d)
            node = node.next

    def print_all(self):
        node = self.head.next

        while node:
            print(node.elem, end='')
            node = node.next
            if node is not None:
                print('->', end='')
            else:
                print()


def reverse_between(linked_list, m, n):
    def solve(start, end, current, d):
        if d == n:
            end.next = current
            start.next = current.next
            return

        new = current.next
        solve(start, end, new, d + 1)
        new.next = current

    last = linked_list.head
    m_node = last.next
    for _ in range(m):
        last = m_node
        m_node = m_node.next
    solve(m_node, last, m_node, m)
    linked_list.print_all()


reverse_between(LinkedList([1, 2, 3, 4, 5, 6, 7]), 0, 5)
