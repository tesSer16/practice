import heapq


def dijkstra(start):
    d = [INF for _ in range(n + 1)]
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


INF = 16
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
data = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, length = map(int, input().split())
    data[a].append([b, length])
    data[b].append([a, length])

print(max([sum([items[i - 1] if datum <= m else 0 for i, datum in enumerate(dijkstra(area))]) for area in range(1, n + 1)]))
