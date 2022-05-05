import sys
import heapq
read = sys.stdin.readline

for _ in range(int(read())):
    n = int(read())
    p = list(map(int, read().split()))
    tree = [[] for _ in range(n + 1)]
    in_degree = [[0, i] for i in range(n + 1)]

    for i in range(n):
        in_degree[p[i]][0] -= 1
    in_degree.sort()

    visited = [1] + [0] * n
    answer = []
    while in_degree:
        v = in_degree.pop()[1]
        if visited[v]:
            continue
        w = p[v - 1]
        path = [v]
        while v != w:
            if visited[w]:
                break
            w, v = p[w - 1], p[v - 1]
            path.append(v)
            visited[v] = 1
        answer.append([len(path), path[::-1]])

    print(len(answer))
    for num, _path in answer:
        print(num)
        print(*_path)
    print()
