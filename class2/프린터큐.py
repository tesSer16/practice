from collections import deque
import sys
input = sys.stdin.readline

for _ in ' ' * int(input()):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    q = deque(list(zip(priority, range(N))))
    priority.sort()

    cnt = 1
    while True:
        if q[0][0] == priority[-1]:
            if q[0][1] == M:
                break
            cnt += 1
            priority.pop()
            q.popleft()
        else:
            q.append(q.popleft())

    print(cnt)
