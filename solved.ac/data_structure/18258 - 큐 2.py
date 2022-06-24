import sys
read = sys.stdin.readline


class Node:
    def __init__(self, data, post=None):
        self.data = data
        self.post = post


class LinkedList:
    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None

    def is_empty(self):
        return +(self.front is None)

    def first(self):
        return self.front.data if self.front else -1

    def last(self):
        return self.rear.data if self.rear else -1

    def popleft(self):
        if self.is_empty():
            return -1

        temp = self.front
        self.front = self.front.post

        self.size -= 1
        if self.size == 0:
            self.rear = None
        return temp.data

    def push(self, x):
        self.size += 1
        temp = Node(x)
        if self.is_empty():
            self.front = temp
            self.rear = temp
            return
        self.rear.post = temp
        self.rear = temp


q = LinkedList()
for _ in range(int(read())):
    c = read().split()
    if c[0] == "push":
        q.push(int(c[1]))
    elif c[0] == "pop":
        print(q.popleft())
    elif c[0] == "size":
        print(q.size)
    elif c[0] == "empty":
        print(q.is_empty())
    elif c[0] == "back":
        print(q.last())
    else:
        print(q.first())
