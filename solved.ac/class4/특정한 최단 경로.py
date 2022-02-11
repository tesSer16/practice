import heapq


def dijkstra(start, end):
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

    return d[end]


INF = 1000 * 1000
N, E = map(int, input().split())
data = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    data[a].append([b, c])
    data[b].append([a, c])

v1, v2 = map(int, input().split())
const = dijkstra(v1, v2)
case1 = dijkstra(1, v1) + dijkstra(v2, N)
case2 = dijkstra(1, v2) + dijkstra(v1, N)

if (case1 == INF and case2 == INF) or const == INF:
    print(-1)
else:
    print(min(case1, case2) + const)
