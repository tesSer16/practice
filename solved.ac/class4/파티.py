import heapq
import sys


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


N, M, X = map(int, input().split())
INF = 100 * 1000
data = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    data[a].append([b, c])

party = dijkstra(X)
good_news = 0
for std in range(1, N + 1):
    if std == X:
        continue
    good_news = max(good_news, dijkstra(std)[X] + party[std])

print(good_news)
