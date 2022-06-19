N = int(input())
d = [0, *map(int, input().split())]
for i in range(2, N + 1):
    d[i] = max([d[j] + d[i-j] for j in range(i)])
print(d[N])
