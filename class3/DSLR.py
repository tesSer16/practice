from collections import deque
import sys


def D(n):
    return (2 * n) % 10000


def S(n):
    return (n - 1) % 10000


def L(n):
    return (n % 1000) * 10 + n // 1000


def R(n):
    return (n % 10) * 1000 + n // 10


def bfs(a, b):
    q = deque([a])
    while q:
        n = q.popleft()
        if n == b:
            return visited[n]

        for k, v in commands.items():
            value = v(n)
            if visited[value] == "1":
                q.append(value)
                visited[value] = visited[n] + k


commands = {'D': D, 'S': S, 'L': L, 'R': R}
for _ in range(int(input())):
    visited = ["1"] * 100001
    A, B = map(int, sys.stdin.readline().split())
    visited[A] = ""
    print(bfs(A, B))
