from collections import deque
import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n = int(read())
    arr = list(map(int, read().split()))
    q = [(deque(arr), deque())]
    d = 0
    while q and d < n:
        nq = []
        for a, p in q:
            if d == 0:
                v = a.popleft()
                nq.append((a + deque(), deque([v])))
                a.appendleft(v)
                w = a.pop()
                nq.append((a + deque(), deque([w])))
            else:
                v = a.popleft()
                if v <= p[-1]:
                    p.appendleft(v)
                    nq.append((a + deque(), p + deque()))
                    p.popleft()
                a.appendleft(v)
                w = a.pop()
                if w <= p[0]:
                    nq.append((a + deque(), p + deque([w])))
        q = nq[::]
        d += 1

    if q:
        print(*q[0][1])
    else:
        print(-1)
