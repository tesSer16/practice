N, M = int(input()), int(input())
board = [list(map(int, input().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            board[i][j] = max(board[i][j], board[i][k] and board[k][j])

arr = list(map(int, input().split()))
for m in range(M - 1):
    if not board[arr[m] - 1][arr[m + 1] - 1]:
        print("NO")
        break
else:
    print("YES")
