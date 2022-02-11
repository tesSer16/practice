from itertools import combinations

N, M = map(int, input().split())
chicken = []
house = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 2:
            chicken.append((i, j))
        elif temp[j] == 1:
            house.append((i, j))

answer = 119150
for selected in combinations(chicken, M):
    case = 0
    for r, c in house:
        case += min([abs(r - a) + abs(c - b) for a, b in selected])

    answer = min(answer, case)

print(answer)
