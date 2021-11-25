from collections import deque
import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n = int(read())
    arr = list(map(int, read().split()))
    q = deque(arr)
    answer = deque()
    for _ in range(n):
        if q[0] > q[-1]:
            answer.appendleft(q.popleft())
        else:
            answer.append(q.pop())

    ans = list(answer)
    check = deque()
    for _ in range(n - 1):
        if answer[0] < answer[-1]:
            check.appendleft(answer.popleft())
        else:
            check.append(answer.pop())

    if list(check + answer) == arr or list(answer + check) == arr:
        print(*ans)
    else:
        print(-1)
