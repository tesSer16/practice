import heapq
import sys
read = sys.stdin.readline


def dijkstra(start):
    d = [INF for _ in range(V + 1)]
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


V, E = map(int, read().split())
INF = V * 10 + 1
data = [[] for _ in range(V + 1)]
start_v = int(input())
for _ in range(E):
    a, b, c = map(int, read().split())
    data[a].append([b, c])

result = dijkstra(start_v)
for i in range(V):
    print(result[i + 1] if result[i + 1] < INF else "INF")
