from collections import deque

N, M = map(int, input().split())
in_degree = [0] * (N + 1)
data = [[] for _ in range(N + 1)]

for _ in range(M):
    n, *arr = map(int, input().split())
    for i in range(1, n):
        data[arr[i - 1]].append(arr[i])
        in_degree[arr[i]] += 1

q = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        q.append(i)

answer = []
while q:
    v = q.popleft()
    answer.append(v)
    for w in data[v]:
        in_degree[w] -= 1
        if in_degree[w] == 0:
            q.append(w)

print(*answer if len(answer) == N else [0])
