def move(d):
    new_board = [[0] * N for _ in range(N)]
    if d == 0:
        for j in range(N):
            stack = []
            for i in range(N):
                if not board[i][j]:
                    continue
                if stack and stack[-1] == [board[i][j]]:
                    stack[-1].append(board[i][j])
                else:
                    stack.append([board[i][j]])

            for k in range(len(stack)):
                new_board[k][j] = sum(stack[k])

    elif d == 1:
        for i in range(N):
            stack = []
            for j in range(N - 1, -1, -1):
                if not board[i][j]:
                    continue
                if stack and stack[-1] == [board[i][j]]:
                    stack[-1].append(board[i][j])
                else:
                    stack.append([board[i][j]])

            for k in range(len(stack)):
                new_board[i][N - 1 - k] = sum(stack[k])

    return new_board


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(*move(1), sep='\n')
