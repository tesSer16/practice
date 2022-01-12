import sys
import heapq
read = sys.stdin.readline


def dijkstra(start):
    d = [INF for _ in range(N + 1)]
    d[start] = 0
    heap = [(0, start)]
    while heap:
        distance, current = heapq.heappop(heap)
        if d[current] < distance:
            continue
        for node, dist in data[current]:
            next_distance = dist - ((dist - distance) // M) * M + 1
            if next_distance < d[node]:
                d[node] = next_distance
                heapq.heappush(heap, (next_distance, node))

    return d


N, M = map(int, read().split())
INF = 1000000000000000000
data = [[] for _ in range(N + 1)]
for i in range(M):
    v1, v2 = map(int, read().split())
    data[v1].append([v2, i])
    data[v2].append([v1, i])

print(dijkstra(1)[N])
