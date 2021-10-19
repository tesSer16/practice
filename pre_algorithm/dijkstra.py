import heapq


def dijkstra(start):
    d = [INF for _ in range(N + 1)]
    d[start] = 0
    heap = [(0, start)]
    while heap:
        distance, current = heapq.heappop(heap)
        print(heap)
        if d[current] < distance:
            continue
        for node, dist in data[current]:
            next_distance = distance + dist
            if next_distance < d[node]:
                d[node] = next_distance
                heapq.heappush(heap, (next_distance, node))

    return d


N = 6
INF = 10000000
graph = [[0 if i == j else INF for j in range(N)] for i in range(N)]
data = [[(2, 2), (3, 5), (4, 1)],
        [(1, 2), (3, 3), (4, 2)],
        [(1, 5), (2, 3), (4, 3), (5, 1), (6, 5)],
        [(1, 1), (2, 2), (3, 3), (5, 1)],
        [(3, 1), (4, 1), (6, 2)],
        [(3, 5), (5, 1)]]

E = len(data)
for i in range(E):
    for datum in data[i]:
        graph[i][datum[0] - 1] = datum[1]

print(*graph, sep='\n')

print(dijkstra(0))
