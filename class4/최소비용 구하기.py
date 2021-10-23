import heapq
import sys
input = sys.stdin.readline


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


N, M = int(input()), int(input())
INF = 1000 * 100000
data = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    data[a].append([b, c])

print(dijkstra(*map(int, input().split())))
