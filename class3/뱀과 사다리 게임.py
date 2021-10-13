import heapq


def dijkstra(start):
    d = [100 for _ in range(100)]
    d[start] = 0
    heap = [(0, start)]
    while heap:
        distance, current = heapq.heappop(heap)
        if d[current] < distance:
            continue
        for data in nodes[current]:
            next_distance = distance + data[1]
            if next_distance < d[data[0]]:
                d[data[0]] = next_distance
                heapq.heappush(heap, (next_distance, data[0]))

    return d


N, M = map(int, input().split())
nodes = [[] for _ in range(100)]
ladder_snake = []
for _ in range(N + M):
    x, y = map(int, input().split())
    nodes[x - 1].append([y - 1, 0])
    ladder_snake.append(x - 1)

for i in range(100):
    if i in ladder_snake:
        continue
    for j in range(1, 7):
        if i + j > 99:
            continue
        nodes[i].append([i + j, 1])

print(dijkstra(0)[99])
