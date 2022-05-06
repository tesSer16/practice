from collections import deque

N = int(input())
time = [0]
data = [[0] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
dp = [0] * (N + 1)

for i in range(N):
    t, *branches, dum = map(int, input().split())
    time.append(t)
    for b in branches:
        data[b].append(i + 1)
    in_degree[i + 1] = len(branches)

q = deque()
for i in range(N):
    if in_degree[i + 1] == 0:
        q.append(i + 1)
        dp[i + 1] = time[i + 1]

while q:
    v = q.popleft()
    for w in data[v]:
        in_degree[w] -= 1
        dp[w] = max(dp[v] + time[w], dp[w])
        if in_degree[w] == 0:
            q.append(w)

print(*dp[1:])
