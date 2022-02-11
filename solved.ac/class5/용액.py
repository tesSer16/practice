N = int(input())
solutions = list(map(int, input().split()))

min_diff = abs(solutions[0] + solutions[-1])
min_i, min_j = 0, N - 1
i, j = 0, N - 1
while i < j:
    diff = solutions[i] + solutions[j]
    if abs(diff) < min_diff:
        min_diff = abs(diff)
        min_i, min_j = i, j

    if diff > 0:
        j -= 1
    elif diff == 0:
        min_i, min_j = i, j
        break
    else:
        i += 1

print(solutions[min_i], solutions[min_j])
