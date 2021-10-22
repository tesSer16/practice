from collections import deque

N, K = map(int, input().split())

q = deque([(N, 0)])
while q:
    current, time = q.popleft()
    if current == K:
        print(time)
        break
    for i, move in enumerate([current * 2, current - 1, current + 1]):
        if 0 <= move <= K:
            q.append((move, time + 1 if i else time))
