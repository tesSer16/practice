import heapq

N = int(input())
graph = [[] for _ in range(N)]

stars = []
for i in range(N):
    x1, y1 = map(float, input().split())
    for j in range(len(stars)):
        x2, y2 = stars[j]
        dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        graph[i].append([dist, j])
        graph[j].append([dist, i])
    stars.append((x1, y1))

heap = graph[0][::]
heapq.heapify(heap)
visited = [1] + [0] * (N - 1)
total_w = 0
while heap:
    w, u = heapq.heappop(heap)
    if not visited[u]:
        total_w += w
        visited[u] = 1
        for w_v, v in graph[u]:
            heapq.heappush(heap, [w_v, v])

print(total_w)
