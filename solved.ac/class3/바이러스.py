import sys
from collections import deque

N, M = int(input()), int(input())
network = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    network[x][y] = network[y][x] = 1


def bfs():
    infected = [1]
    possible_cases = deque([1])
    while possible_cases:
        current_pc = possible_cases.popleft()
        for i in range(N + 1):
            if network[current_pc][i] and i not in infected:
                possible_cases.append(i)
                infected.append(i)

    return len(infected)


print(bfs() - 1)
