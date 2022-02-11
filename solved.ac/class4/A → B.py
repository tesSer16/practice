from collections import deque


A, B = map(int, input().split())


def bfs(start, end):
    q = deque([(start, 1)])
    while q:
        current, depth = q.popleft()
        if current == end:
            return depth

        if current * 2 <= end:
            q.append((current * 2, depth + 1))
        if current * 10 + 1 <= end:
            q.append((current * 10 + 1, depth + 1))

    return -1


print(bfs(A, B))
