from collections import deque
import sys
read = sys.stdin.readline


def dfs(d, a, p):
    if answer[0]:
        return
    if d == n:
        answer[0] = p
        return
    if d == 0:
        v = a.popleft()
        dfs(1, a + deque(), deque([v]))
        a.appendleft(v)
        w = a.pop()
        dfs(1, a + deque(), deque([w]))
    else:
        v = a.popleft()
        if v <= p[-1]:
            p.appendleft(v)
            dfs(d + 1, a + deque(), p + deque())
        a.appendleft(v)
        w = a.pop()
        if w <= p[0]:
            dfs(d + 1, a + deque(), p + deque([w]))


for _ in range(int(read())):
    n = int(read())
    arr = list(map(int, read().split()))
    answer = [[]]
    dfs(0, deque(arr), deque())
    if answer[0]:
        print(*answer[0])
    else:
        print(-1)
