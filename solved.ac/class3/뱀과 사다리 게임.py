import heapq


def dijkstra(start):
    d = [100 for _ in range(100)]
    d[start] = 0
    heap = [(0, start)]
    while heap:
        distance, current = heapq.heappop(heap)
        if d[current] < distance:
            continue
        for idx in range(100):
            next_distance = distance + graph[current][idx]
            if next_distance < d[idx]:
                d[idx] = next_distance
                heapq.heappush(heap, (next_distance, idx))

    return d


N, M = map(int, input().split())
graph = [[0 if i == j else 100 for j in range(100)] for i in range(100)]
ladder_snake = []
for _ in range(N + M):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 0
    ladder_snake.append(x - 1)

for i in range(100):
    if i in ladder_snake:
        continue
    for j in range(1, 7):
        if i + j > 99:
            continue
        graph[i][i + j] = 1

print(dijkstra(0)[99])
