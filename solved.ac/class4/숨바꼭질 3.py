from collections import deque

N, K = map(int, input().split())
MAX = 100001
visited = [MAX] * MAX
visited[N] = 0
q = deque([N])
while q:
    current = q.popleft()
    if current == K:
        print(visited[K])
        break
    for i, next_x in enumerate([current * 2, current - 1, current + 1]):
        next_time = visited[current] + 1 if i else visited[current]
        if 0 <= next_x < MAX and next_time < visited[next_x]:
            visited[next_x] = next_time
            q.append(next_x)
