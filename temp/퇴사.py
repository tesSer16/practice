N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]
result = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    arr = [result[j] for j in range(i + data[i][0], N + 1)]
    result[i] = data[i][1] + max(arr) if arr else 0

print(max(result))
