import heapq
import sys
read = sys.stdin.readline


def dijkstra():
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
                mem[node] = mem[current] + [node]
                d[node] = next_distance
                heapq.heappush(heap, (next_distance, node))

    return d[end]


N, M = int(read()), int(read())
INF = 1000 * 100000
data = [[] for _ in range(N + 1)]
mem = [[i] for i in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, read().split())
    data[a].append([b, c])

start, end = map(int, read().split())
print(dijkstra())
print(len(mem[end]))
print(*mem[end])
