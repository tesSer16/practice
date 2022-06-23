class Node:
    def __init__(self, data, prev=None, post=None):
        self.data = data
        self.prev = prev
        self.post = post


class DoublyLinkedList:
    def __init__(self, seq):
        self.front = None
        self.rear = None
        self.length = 0
        for s in seq:
            self.append(s)

    def append(self, data):
        temp = Node(data, self.rear)
        if self.front is None:
            self.front = temp
            self.rear = temp
        else:
            self.rear.post = temp
            self.rear = temp

        self.length += 1

    def popleft(self):
        if self.front == self.rear:
            self.front = self.rear = None
            return
        temp = self.front
        self.front = self.front.post
        self.front.prev = None

        self.length -= 1

        return temp

    def rotate_right(self):
        if self.front == self.rear:
            return
        temp = self.rear
        self.rear = self.rear.prev
        self.rear.post = None
        temp.prev = None
        temp.post = self.front
        self.front.prev = temp
        self.front = temp

    def rotate_left(self):
        if self.front == self.rear:
            return
        temp = self.front
        self.front = temp.post
        self.front.prev = None
        temp.post = None
        temp.prev = self.rear
        self.rear.post = temp
        self.rear = temp

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.post

        print()

    def find(self, data):
        temp = self.front
        cnt = 0
        while temp and temp.data != data:
            temp = temp.post
            cnt += 1

        return cnt if temp else -1


N, M = map(int, input().split())
q = DoublyLinkedList(range(1, N + 1))
result = 0
for m in map(int, input().split()):
    t = q.find(m)
    num, f = [(t, lambda x: x.rotate_left()), (q.length - t, lambda x: x.rotate_right())][2 * t > q.length]
    for _ in range(num):
        f(q)
    q.popleft()
    result += num

print(result)
