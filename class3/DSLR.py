from collections import deque
import sys


def bfs(a, b):
    q = deque([a])
    while q:
        n = q.popleft()
        if n == b:
            return

        for k, v in commands.items():
            value = v(n)
            if visited[value] == 0:
                q.append(value)
                visited[value] = (n, k)


commands = {'D': lambda x: (2 * x) % 10000,
            'S': lambda x: (x - 1) % 10000,
            'L': lambda x: (x % 1000) * 10 + x // 1000,
            'R': lambda x: (x % 10) * 1000 + x // 10}
for _ in range(int(input())):
    visited = [0] * 10001
    A, B = map(int, sys.stdin.readline().split())
    visited[A] = (0, '')
    bfs(A, B)
    answer = []
    while B != A:
        answer.append(visited[B][1])
        B = visited[B][0]

    for _ in range(len(answer)):
        print(answer.pop(), end="")
    print()
