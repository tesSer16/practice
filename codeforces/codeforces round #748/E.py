import sys
from collections import deque
read = sys.stdin.readline

for _ in range(int(read())):
    read()
    n, k = map(int, read().split())
    data = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    for _ in range(n - 1):
        v, w = map(int, read().split())
        data[v].append(w)
        data[w].append(v)
        in_degree[v] += 1
        in_degree[w] += 1

    q = deque()
    size = 0
    for v in range(1, n + 1):
        if in_degree[v] == 1:
            q.append(v)
            size += 1

    deleted = [0] * (n + 1)
    num = n
    for _ in range(k):
        if num == 1 or num == 2 or num == 0:
            num = 0
            break
        new_size = 0
        for _ in range(size):
            v = q.popleft()
            deleted[v] = 1
            num -= 1
            for w in data[v]:
                if not deleted[w]:
                    in_degree[w] -= 1
                    if in_degree[w] == 1:
                        q.append(w)
                        new_size += 1

        size = new_size

    print(num)
