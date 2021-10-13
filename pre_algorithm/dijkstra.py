import heapq


def dijkstra(start):
    d = [INF for _ in range(N)]
    d[start] = 0
    heap = [(0, start)]
    while heap:
        distance, current = heapq.heappop(heap)
        print(heap)
        if d[current] < distance:
            continue
        for i in range(N):
            next_distance = distance + graph[current][i]
            if next_distance < d[i]:
                d[i] = next_distance
                heapq.heappush(heap, (next_distance, i))

    return d


N = 6
INF = 10000000
graph = [[0 if i == j else INF for j in range(N)] for i in range(N)]
nodes = [[(2, 2), (3, 5), (4, 1)],
         [(1, 2), (3, 3), (4, 2)],
         [(1, 5), (2, 3), (4, 3), (5, 1), (6, 5)],
         [(1, 1), (2, 2), (3, 3), (5, 1)],
         [(3, 1), (4, 1), (6, 2)],
         [(3, 5), (5, 1)]]

for i in range(len(nodes)):
    for node in nodes[i]:
        graph[i][node[0] - 1] = node[1]

print(*graph, sep='\n')

print(dijkstra(0))
