import sys
from collections import deque
read = sys.stdin.readline

for _ in range(int(read())):
    n = int(read())
    q = deque([(1, n)])
    answer = [0, 0, 0]
    for _ in range(40):
        if not all(answer):
            break
        l, r = q.popleft()
        print(f"? {l} {r}")
        sys.stdout.flush()

        ans = int(read())
        if ans == -1:
            exit()


