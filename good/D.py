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
            next_distance = distance + dist
            if next_distance < d[node]:
                d[node] = next_distance
                heapq.heappush(heap, (next_distance, node))

    return d


N, M = map(int, read().split())
INF = float('inf')
data = [[] for _ in range(N + 1)]
for i in range(M):
    v1, v2 = map(int, read().split())
    data[v1].append([v2, i + 1])
    data[v2].append([v1, i + 1])

print(dijkstra(1)[N])
