import heapq


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


INF = 987654321
N, E = map(int, input().split())
data = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    data[a].append([b, c])
    data[b].append([a, c])

v1, v2 = map(int, input().split())
s1 = dijkstra(1)
sv1 = dijkstra(v1)
const = sv1[v2]
case1 = s1[v1] + dijkstra(v2)[N]
case2 = s1[v2] + sv1[N]

print(const, case1, case2)
if (case1 >= INF and case2 >= INF) or const == INF:
    print(-1)
else:
    print(min(case1, case2) + const)
