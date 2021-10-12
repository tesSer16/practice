import sys
sys.setrecursionlimit(10**6)


def check(x, y, color=''):
    if 0 <= x < N and 0 <= y < N:
        if color == board[x][y] and not check_board[x][y]:
            weak_board[x][y] = 1 if color == 'R' or color == 'G' else 0
            check_board[x][y] = 1
        elif color == '' and weak_board[x][y]:
            weak_board[x][y] = 0
        else:
            return
        check(x - 1, y, color)
        check(x + 1, y, color)
        check(x, y - 1, color)
        check(x, y + 1, color)


N = int(input())
board = [list(sys.stdin.readline()) for _ in range(N)]
check_board = [[0] * N for _ in range(N)]
weak_board = [[0] * N for _ in range(N)]
color_cnt = {'R': 0, 'G': 0, 'B': 0, 'RG': 0}

for i in range(N):
    for j in range(N):
        if not check_board[i][j]:
            check(i, j, board[i][j])
            color_cnt[board[i][j]] += 1

for i in range(N):
    for j in range(N):
        if weak_board[i][j]:
            check(i, j)
            color_cnt['RG'] += 1

print(color_cnt['R'] + color_cnt['G'] + color_cnt['B'], color_cnt['B'] + color_cnt['RG'])
