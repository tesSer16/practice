from collections import deque

N, M = map(int, input().split())
c_num, *c_list = map(int, input().split())
data = []

graph = [[0] * N for _ in range(N)]
affected = [0 for _ in range(N)]
for c in c_list:
    affected[c - 1] = 1

for _ in range(M):
    dum, *datum = map(int, input().split())
    for i in range(len(datum)):
        for j in range(i + 1, len(datum)):
            graph[datum[i] - 1][datum[j] - 1] = graph[datum[j] - 1][datum[i] - 1] = 1
    data.append(datum)

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = max(graph[i][j], graph[i][k] & graph[k][j])

q = deque(c_list)
while q:
    c = q.popleft()
    for idx in range(N):
        if graph[c - 1][idx] and not affected[idx]:
            q.append(idx + 1)
            affected[idx] = 1

available = 0
for datum in data:
    for d in datum:
        if affected[d - 1]:
            break
    else:
        available += 1

print(available)
