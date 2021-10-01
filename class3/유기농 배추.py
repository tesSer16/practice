import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1


for i in range(N):
    for j in range(M):
        print(ground[i][j], end=" ")
    print()
