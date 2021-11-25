string = input()
n = len(string)
P = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n - i):
        if string[j] == string[j + i]:
            if i <= 1:
                P[j][j + i] = 1
            else:
                P[j][j + i] = P[j + 1][j + i - 1]

F = [i + 1 for i in range(n)]
for end in range(n):
    for start in range(end + 1):
        if P[start][end]:
            F[end] = min(F[end], F[start - 1] + 1) if start else 1

print(F[n - 1])
