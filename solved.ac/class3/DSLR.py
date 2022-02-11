from collections import deque
import sys


def bfs(a, b):
    q = deque([a])
    while q:
        n = q.popleft()
        if n == b:
            return

        for di in range(4):
            value = commands[di](n)
            if visited[value] == 0:
                q.append(value)
                visited[value] = (n, di)


commands = [lambda x: (2 * x) % 10000,
            lambda x: (x - 1) % 10000,
            lambda x: (x % 1000) * 10 + x // 1000,
            lambda x: (x % 10) * 1000 + x // 10]

for _ in range(int(input())):
    visited = [0] * 10001
    A, B = map(int, sys.stdin.readline().split())
    bfs(A, B)
    answer = []
    cnt = 0
    while B != A:
        answer.append(visited[B][1])
        B = visited[B][0]
        cnt += 1

    for _ in range(cnt):
        print("DSLR"[answer.pop()], end="")
    print()
