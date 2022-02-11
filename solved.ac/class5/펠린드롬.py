import sys
input = sys.stdin.readline


N = int(input())
string = [*map(int, input().split())]

P = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N - i):
        if string[j] == string[j + i]:
            if i <= 1:
                P[j][j + i] = 1
            else:
                P[j][j + i] = P[j + 1][j + i - 1]


for _ in range(int(input())):
    S, E = map(int, input().split())
    print(P[S - 1][E - 1])
