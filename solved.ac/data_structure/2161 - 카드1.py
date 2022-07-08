from collections import deque

N = int(input())
q = deque([*range(1, N + 1)])
for _ in range(N - 1):
    print(q.popleft())
    q.append(q.popleft())

print(q[0])
