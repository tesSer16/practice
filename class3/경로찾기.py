N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = max(graph[i][j], graph[i][k] & graph[k][j])

for g in graph:
    print(*g)
