def partial_sum():
    for i in range(N):
        for j in range(N - i):
            if i == 0:
                value = num_list[i]
            else:
                value = matrix[i - 1][j] + matrix[i][j - 1]
            if value >= S:
                return i + 1
            matrix[i][j] = value

    return 0


N, S = map(int, input().split())
num_list = list(map(int, input().split()))
matrix = [[0] * N for _ in range(N)]
print(partial_sum())
