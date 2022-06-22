import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data, prev=None, post=None):
        self.data = data
        self.prev = prev
        self.post = post


class LinkedList:
    def __init__(self, seq):
        self.front = None
        self.rear = None
        self.cursor = None
        for s in seq:
            self.insert_left(s)

    def insert_left(self, data):
        # empty insert
        if self.front is None:
            temp = Node(data)
            self.front = temp
            self.rear = temp
        # front insert
        elif self.cursor is None:
            temp = Node(data, None, self.front)
            self.front.prev = temp
            self.front = temp
        # rear insert
        elif self.cursor.post is None:
            temp = Node(data, self.cursor, None)
            self.rear = temp
            self.cursor.post = temp
        # default
        else:
            temp = Node(data, self.cursor, self.cursor.post)
            self.cursor.post.prev = temp
            self.cursor.post = temp
        self.cursor = temp

    def delete_left(self):
        if self.cursor is None:
            return

        # make empty
        if self.cursor.prev is None and self.cursor.post is None:
            self.front = None
            self.rear = None
        # delete front
        elif self.cursor.prev is None:
            self.front = self.cursor.post
            self.front.prev = None
        # delete rear
        elif self.cursor.post is None:
            self.rear = self.cursor.prev
            self.cursor.prev.post = None
        # default case
        else:
            self.cursor.prev.post = self.cursor.post
            self.cursor.post.prev = self.cursor.prev

        self.cursor = self.cursor.prev

    def cursor_right(self):
        if self.cursor is None:
            self.cursor = self.front
            return

        if self.cursor.post:
            self.cursor = self.cursor.post

    def cursor_left(self):
        if self.cursor:
            self.cursor = self.cursor.prev

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end="")
            temp = temp.post

        print()


string = input().strip()
LL = LinkedList(string)  # 변수명 고민은 LL
for _ in range(int(input())):
    c = input()
    if c[0] == 'L':
        LL.cursor_left()
    elif c[0] == 'D':
        LL.cursor_right()
    elif c[0] == 'B':
        LL.delete_left()
    else:
        LL.insert_left(c[2])

LL.print()
