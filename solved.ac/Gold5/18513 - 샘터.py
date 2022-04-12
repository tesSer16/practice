from collections import deque

N, K = map(int, input().split())
visited = set()
lake = list(map(int, input().split()))
q = deque()
for idx in lake:
    visited.add(idx)
    q.append((idx, 0))

ans = cnt = 0
while q:
    x, d = q.popleft()
    for dx in [-1, 1]:
        nx = x + dx
        if nx not in visited:
            q.append((nx, d + 1))
            visited.add(nx)
            ans += d + 1
            cnt += 1

            if cnt == K:
                print(ans)
                exit(0)
